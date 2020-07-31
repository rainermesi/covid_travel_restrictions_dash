import plotly.express as px
df = px.data.tips()
fig = px.sunburst(df, path=['day', 'time', 'sex'], values='total_bill')

import dash
import dash_core_components as dcc
import dash_html_components as html

# for deployment, pass app.server (which is the actual flask app) to WSGI etc
app = dash.Dash()

app.layout = html.Div(
    children=[
    html.H1(children='Dash Demo'),

    html.Div(children='''
        Plotly Dashb running on pythonanywhere
    '''),

    html.Div(
    dcc.Graph(id='i',figure=fig)
)
]
)