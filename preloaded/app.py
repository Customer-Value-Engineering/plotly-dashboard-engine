import dash
import dash_html_components as html
import dash_design_kit as ddk
import plotly.express.data as data
import dashboard_engine as dbe


app = dash.Dash(__name__)
conn_provider = dbe.PandasConnectionProvider(data.gapminder())
engine = dbe.DashboardEngine(app, conn_provider)

config = (
    dbe.CanvasConfig()
    .add_card(dbe.elements.Bar(x="continent", y="pop", color="continent"))
    .add_card(
        [
            dbe.elements.Dropdown(value="year", clearable=False),
            dbe.elements.Table(
                columns=[
                    dict(column="continent"),
                    dict(column="lifeExp", aggregator="mean"),
                    dict(column="gdpPercap", aggregator="mean"),
                ]
            ),
        ]
    )
    .add_card(dbe.elements.Indicator(value="lifeExp", aggregator="mean"), h=2)
    .add_card(dbe.elements.Indicator(value="pop", aggregator="sum"), h=2)
)

app.layout = ddk.App(
    children=html.Div(
        engine.make_state_and_canvas(
            id="sc", elements=config.elements, arrangement=config.arrangement
        )
    ),
)

if __name__ == "__main__":
    app.run_server(debug=True)
