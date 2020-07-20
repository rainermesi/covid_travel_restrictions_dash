import plotly.express as px
df = px.data.gapminder().query("year == 2007")
fig = px.sunburst(df, path=['continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'])

fig.show()

import plotly.express as px
df = px.data.tips()
fig = px.sunburst(df, path=['time', 'sex'], values='total_bill',color='day')
fig.show()

df = px.data.tips()
fig = px.sunburst(df, path=['sex', 'day', 'time'], values='total_bill', color='time',
                  color_discrete_map={'(?)':'black', 'Lunch':'gold', 'Dinner':'darkblue'})
fig.show()

import pandas as pd

tdf = pd.read_csv(r'c:\users\raine\downloads\2019_kulude_osakaalud.csv')
tdf.head()
tdf = tdf[['valdkond','allsektor','osakaal']]

fig = px.sunburst(tdf, path=['valdkond','allsektor'],values='osakaal')
fig.show()