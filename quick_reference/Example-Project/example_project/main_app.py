
import dash
import dash_table
import dash_daq as daq
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State



external_stylesheets = [
    dbc.themes.YETI,
    # 'https://codepen.io/chriddyp/pen/bWLwgP.css',
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    className="main_window",
    children=[]
)


if __name__ == '__main__':
    app.run_server(debug=True)
