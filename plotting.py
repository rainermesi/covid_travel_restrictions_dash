import plotly.express as px
import pandas as pd

df = px.data.gapminder().query("year == 2007")
fig = px.sunburst(df, path=['continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'])

fig.show()


df = px.data.tips()
fig = px.sunburst(df, path=['time', 'sex'], values='total_bill',color='day')
fig.show()

df = px.data.tips()
fig = px.sunburst(df, path=['sex', 'day', 'time'], values='total_bill', color='time',
                  color_discrete_map={'(?)':'black', 'Lunch':'gold', 'Dinner':'darkblue'})
fig.show()


tdf = pd.read_csv(r'c:\users\raine\downloads\2019_kulude_osakaalud.csv')
tdf.head()
tdf = tdf[['valdkond','allsektor','osakaal']]

fig = px.sunburst(tdf, path=['valdkond','allsektor'],values='osakaal')
fig.show()

### country by country barchart
#prep dataframe

df = pd.read_csv('union_001.csv')
#only keel latest date rows
df = df[df['load_dt'] == (max(df['load_dt']))]
#comma to fullstop
df['metric'] = df['metric'].str.replace(',','.')
df.head()
df
#convert to float
df['metric'] = df['metric'].astype(float)
#sort values for barchart
df = df.sort_values('metric',ascending=True)
#keep only necessary columns
df = df[['country','metric','load_dt']]

#plot barchart
fig = px.bar(df,x='country',y='metric')
fig.show()