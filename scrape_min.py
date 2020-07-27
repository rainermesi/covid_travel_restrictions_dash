import requests
from lxml import html
import pandas as pd

#variables
URL = 'https://vm.ee/et/teave-riikide-ja-eneseisolatsiooninouete-kohta-euroopast-saabujatele'
curr_fn = str(pd.datetime.today().date())+'_fmin.csv'

data_dict = {
    'country': [],
    'metric': []
}

#data cleaning function
def clean_data(data):
    temp_df = pd.read_csv(data)[['country','metric','load_dt']]
    temp_df['metric'] = temp_df['metric'].str.replace('*','')
    temp_df['metric'] = temp_df['metric'].str.replace(',','.')
    temp_df['metric'] = temp_df['metric'].astype(float)
    temp_df['load_dt'] = pd.to_datetime(temp_df['load_dt']).dt.date
    pd.concat([pd.read_csv('union_001.csv'),temp_df])[['country','metric','load_dt']].to_csv('union_001.csv',index=False)

#get web content function

def get_data(x):
    page = requests.get(x)
    tree = html.fromstring(page.content)
    update_dt = tree.xpath('//*[@id="node-article-53150"]/div[1]/div/div/div/h3[2]')
    countries = tree.xpath('//*[@id="node-article-53150"]/div[1]/div/div/div/ul[3]')
    for i in countries:
        for elem in i:
            #last element of the split (for country names that are 1+ words long()
            temp_slc = len(elem.text_content().split())-1
            if len(elem.text_content().split()) > 2:
                data_dict['country'].append(elem.text_content().split()[0]+' '+elem.text_content().split()[1])
                data_dict['metric'].append(elem.text_content().split()[temp_slc])
            else:
                data_dict['country'].append(elem.text_content().split()[0])
                data_dict['metric'].append(elem.text_content().split()[temp_slc])
    data_df = pd.DataFrame.from_dict(data_dict)
    data_df['load_dt'] = pd.datetime.today().date()
    data_df.to_csv(curr_fn)

get_data(URL)
clean_data(curr_fn)