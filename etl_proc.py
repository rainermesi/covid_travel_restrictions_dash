import pandas as pd

curr_fn = str(pd.datetime.today().date())+'_fmin.csv'

#check if file is ok
#make tz to dt
#convert metric to float
#remove extra columns
#union data
#use functions

#failed union

pd.concat([pd.read_csv('union_001.csv'),pd.read_csv(curr_fn)]).to_csv('union_002.csv')

new_df = pd.read_csv('2020-07-26_fmin.csv')
new_df.head()
u_df = pd.read_csv('union_001.csv')

#to datetime conversion
u_df['load_dt'] = pd.to_datetime(u_df['load_dt']).dt.normalize()

u_df.to_csv('union_001.csv')

temp_df_1 = pd.read_csv(
    '1007_fmin.csv'
)

temp_df_2 = pd.read_csv(
    '2007_fmin.csv'
)

temp_df_3 = pd.concat([temp_df_1,temp_df_2])

temp_df_3.info()

temp_df_3.to_csv('union_001.csv')