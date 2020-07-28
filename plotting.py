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

#optional subset of 5 countries
sub = df['country'].isin(['Austria','Belgia','Bulgaaria','Hispaania','Holland'])

df_s = df[sub]

#normalize datetimes (this needs to be preprocessed)
df_s['load_dt'] = pd.to_datetime(df_s['load_dt']).dt.normalize()
df['load_dt'] = pd.to_datetime(df['load_dt']).dt.normalize()


#plot barchart
fig_bc = px.bar(df,x='country',y='metric')
fig_bc.show()

#plot faceted linechart
fig_lc = px.line(df,x='load_dt',
y='metric',
range_x=['2020-07-10','2020-07-21'],
facet_row='country',
height=4200,
facet_row_spacing=0.01,
) 
fig_lc.update_yaxes(matches=None)
fig_lc.show()

#try out a faceted line chart

df = pd.read_csv('union_001.csv')

fig = px.line(df, x='load_dt', y='metric', facet_col='country', facet_col_wrap = 7,
            facet_row_spacing = 0.04,
            facet_col_spacing = 0.04,
            height=600,width=800,
            title='Corona travel index in Europe')
fig.for_each_annotation(lambda a: a.update(text=a.text.split('=')[-1]))
fig.update_yaxes(showticklabels=True)
fig.show()