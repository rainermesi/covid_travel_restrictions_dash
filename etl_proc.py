import pandas as pd

curr_fn = str(pd.datetime.today().date())+'_fmin.csv'

#check if file is ok
def clean_data(data):
    temp_df = pd.read_csv(data)[['country','metric','load_dt']]
    temp_df['metric'] = temp_df['metric'].str.replace('*','')
    temp_df['metric'] = temp_df['metric'].str.replace(',','.')
    temp_df['metric'] = temp_df['metric'].astype(float)
    temp_df['load_dt'] = pd.to_datetime(temp_df['load_dt']).dt.date
    pd.concat([pd.read_csv('union_001.csv'),temp_df])[['country','metric','load_dt']].to_csv('union_001.csv',index=False)

clean_data(curr_fn)

temp_df = pd.read_csv('union_001.csv')

len(temp_df.country.unique())