import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Laines Dashboard",
)

app.layout = html.Div(
    className="dashboard-wrapper",
    children=[
        dash.page_container,
    ],
)

server = app.server 

if __name__ == "__main__":
    app.run(debug=True)