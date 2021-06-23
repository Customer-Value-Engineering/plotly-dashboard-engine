import json
import plotly
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_html_components as html
import dash_core_components as dcc
import dash_snapshots
import dash_design_kit as ddk
import dashboard_engine as dbe
from plotly.express import data
from theme import theme
import os

os.environ["SNAPSHOT_DATABASE_URL"] = os.environ.get(
    "SNAPSHOT_DATABASE_URL",
    os.environ.get("DATABASE_URL", "sqlite:///:memory:"),
)


app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server  # expose server variable for Procfile
dfs = dict(
    gapminder=data.gapminder(),
    tips=data.tips(),
)
conn_provider = dbe.PandasConnectionProvider(dfs)
engine = dbe.DashboardEngine(app, conn_provider)
snap = dash_snapshots.DashSnapshots(app)

app.layout = ddk.App(
    theme=theme,
    children=[dcc.Location(id="url"), html.Div(id="content")],
    show_editor=True,
)


@app.callback(Output("content", "children"), [Input("url", "pathname")])
def router(pathname):
    if pathname is None or pathname == snap.relpath("/"):
        return archive_page()
    if pathname in snap.relpath("/create/"):
        return dashboard_page(None, False)
    if pathname.startswith(snap.relpath("/snapshot-")):
        snapshot_id = pathname.replace(snap.relpath("/"), "", 1).replace("/edit", "")
        return dashboard_page(snapshot_id, not pathname.endswith("/edit"))
    return "404"


def archive_page():
    keys = dash_snapshots.constants.KEYS
    return html.Div(
        [
            ddk.Header(
                children=[
                    ddk.Title("Dashboard Lifecycle App (powered by Dashboard Engine)"),
                    ddk.Menu([dcc.Link("New Dashboard", href=snap.relpath("/create"))]),
                ]
            ),
            ddk.Card(
                children=[
                    ddk.CardHeader(title="Saved Dashboards"),
                    snap.ArchiveTable(
                        columns=[
                            {"id": keys["snapshot_id"], "name": "id"},
                            {"id": "title", "name": "Title"},
                            {"id": keys["username"], "name": "Created By"},
                            {"id": keys["created_time"], "name": "Created On"},
                        ],
                        version=1,
                    ),
                ]
            ),
        ]
    )


def dashboard_page(snapshot_id, show_mode):
    if snapshot_id:
        new = False
        state_and_canvas = snap.snapshot_get(snapshot_id)
        title = snap.meta_get(snapshot_id, "title", "")
        connection_params = snap.meta_get(snapshot_id, "connection_params", "")
    else:
        snapshot_id = ""
        new = True
        title = ""
        connection_params = "gapminder"
        state_and_canvas = engine.make_state_and_canvas(
            id="sc", connection_params=connection_params
        )

    hide = dict(display="none")

    menu_items = [
        html.Button("Save", id="save", style=hide if show_mode else None),
        html.Button("Save a Copy", id="fork", style=hide if new or show_mode else None),
        html.Button("Delete", id="delete", style=hide if new or show_mode else None),
        dcc.Link(
            "Edit",
            href=snap.relpath("/" + snapshot_id + "/edit"),
            style=None if show_mode else hide,
        ),
        dcc.Link("Back to List", href=snap.relpath("/")),
    ]

    if show_mode:
        state_and_canvas[1]["props"]["editable"] = False

    return html.Div(
        [
            ddk.Header(
                children=[
                    ddk.Title("Dashboard Lifecycle App (powered by Dashboard Engine)"),
                    ddk.Menu(menu_items),
                ]
            ),
            ddk.ControlCard(
                orientation="horizontal",
                style=hide if show_mode else None,
                children=[
                    ddk.ControlItem(
                        dcc.Input(id="dashboard-title", value=title, type="text"),
                        label="Title",
                    ),
                    ddk.ControlItem(
                        dcc.Dropdown(
                            id="dashboard-connstr",
                            value=connection_params,
                            disabled=(not new),
                            options=[
                                {"label": x, "value": x} for x in list(dfs.keys())
                            ],
                        ),
                        label="Dataset",
                    ),
                ],
            ),
            html.H2(title, style=dict(marginLeft="20px") if show_mode else hide),
            html.Div(id="snapshot_id", children=snapshot_id, style=hide),
            html.Div(id="state_and_canvas", children=state_and_canvas),
        ]
    )


@app.callback(
    Output("url", "href"),
    Input("save", "n_clicks"),
    Input("fork", "n_clicks"),
    Input("delete", "n_clicks"),
    State("state_and_canvas", "children"),
    State("snapshot_id", "children"),
    State("dashboard-title", "value"),
    State("dashboard-connstr", "value"),
)
def lifecycle(
    n_save_clicks,
    n_fork_clicks,
    n_delete_clicks,
    state_and_canvas,
    snapshot_id,
    title,
    connection_params,
):
    trigger = dash.callback_context.triggered[0]["prop_id"]
    if trigger == "save.n_clicks" and n_save_clicks:
        if not snapshot_id:
            snapshot_id = snap.snapshot_save(state_and_canvas)
        else:  # overwrite
            data = json.dumps(state_and_canvas, cls=plotly.utils.PlotlyJSONEncoder)
            snap.save_blob(snapshot_id, "layout-json", data)
    elif trigger == "fork.n_clicks" and n_fork_clicks:
        snapshot_id = snap.snapshot_save(state_and_canvas)
    elif trigger == "delete.n_clicks" and n_delete_clicks:
        snap.snapshot_delete(snapshot_id)
        return snap.relpath("/")
    else:
        raise PreventUpdate

    snap.meta_update(snapshot_id, {"title": title})
    snap.meta_update(snapshot_id, {"connection_params": connection_params})
    return snap.relpath("/" + snapshot_id)


@app.callback(
    Output("state_and_canvas", "children"),
    Input("dashboard-connstr", "value"),
    prevent_initial_call=True,
)
def change_dataset(connection_params):
    return engine.make_state_and_canvas(id="sc", connection_params=connection_params)


if __name__ == "__main__":
    app.run_server(debug=True)
