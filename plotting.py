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
facet_col='country',
facet_col_wrap=6,
facet_row='country',
#range_x=['2020-07-10','2020-07-21'],
height=2200,
facet_row_spacing=0.01
) 
fig_lc.update_yaxes(matches=None)
fig_lc.show()

df_iso_cd = pd.read_csv('country_cd_iso.csv',delimiter=';')
df_metrics = pd.read_csv('union_001.csv')
df_metrics = df_metrics[df_metrics['load_dt'] == (max(df_metrics['load_dt']))]

df_merged = pd.merge(df_metrics,df_iso_cd,how='left',on='country')

fig = px.choropleth(df_merged,locations='iso_cd',
                    color='metric',
                    hover_name='country',
                    scope='europe',
                    height=600,
                    width=800,
                    range_color=(0,43),
                    color_continuous_scale=px.colors.sequential.Peach)

fig.show()