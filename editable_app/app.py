import dash
import dash_html_components as html
import dash_snapshots
from dash.dependencies import Input, Output, State
import dash_design_kit as ddk
import plotly.express.data as data
import dashboard_engine as dbe
import os

os.environ["SNAPSHOT_DATABASE_URL"] = os.environ.get(
    "SNAPSHOT_DATABASE_URL",
    os.environ.get("DATABASE_URL", "sqlite:///:memory:"),
)

app = dash.Dash(__name__)
conn_provider = dbe.PandasConnectionProvider(data.gapminder())
engine = dbe.DashboardEngine(app, conn_provider)
snap = dash_snapshots.DashSnapshots(app)


def layout_with_latest_snapshot():
    try:
        state_and_canvas = snap.snapshot_get(snap.snapshot_list()[0])
    except Exception:  # no saved snapshots yet
        state_and_canvas = engine.make_state_and_canvas(id="sc")

    return ddk.App(
        children=[
            html.Button("Save", id="save"),
            html.Div(children=state_and_canvas, id="state_and_canvas"),
        ]
    )


app.layout = layout_with_latest_snapshot


@app.callback(
    Output("state_and_canvas", "children"),
    Input("save", "n_clicks"),
    State("state_and_canvas", "children"),
    prevent_initial_call=True,
)
def lifecycle(n_save_clicks, state_and_canvas):
    snap.snapshot_save(state_and_canvas)
    return state_and_canvas


if __name__ == "__main__":
    app.run_server(debug=True)
