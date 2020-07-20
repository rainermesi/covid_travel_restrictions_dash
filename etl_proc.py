import pandas as pd

temp_df_1 = pd.read_csv(
    '1007_fmin.csv'
)

temp_df_2 = pd.read_csv(
    '2007_fmin.csv'
)

temp_df_3 = pd.concat([temp_df_1,temp_df_2])

temp_df_3.info()

temp_df_3.to_csv('union_001.csv')