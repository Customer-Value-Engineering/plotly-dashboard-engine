import dash
import dash_design_kit as ddk
import dashboard_engine as dbe
import plotly.express.data as data

df = data.gapminder()

app = dash.Dash(__name__)
conn_provider = dbe.PandasConnectionProvider(df)
engine = dbe.DashboardEngine(app, conn_provider)
state, canvas = engine.make_state_and_canvas(id="sc")
app.layout = ddk.App(children=[state, canvas])

if __name__ == "__main__":
    app.run_server(debug=True)
