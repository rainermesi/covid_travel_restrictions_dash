import plotly.express as px
import pandas as pd
df = pd.read_csv('/home/rainermesi/Documents/f_min_scrape/union_001.csv')
df = df[df['load_dt'] == (max(df['load_dt']))]
df = df.sort_values('metric',ascending=True)
fig_bc = px.bar(df,x='country',y='metric')

fig_lc = px.line(df,x='load_dt',
y='metric',
facet_col='country',
facet_col_wrap=6,
facet_row='country',
height=2200,
facet_row_spacing=0.01
) 
fig_lc.update_yaxes(matches=None)

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
    dcc.Graph(id='i',figure=fig_bc)
)
]
)