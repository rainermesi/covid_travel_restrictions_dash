import requests
from lxml import html
import pandas as pd

cur_dt = str(pd.datetime.today().date())
URL = 'https://vm.ee/et/teave-riikide-ja-eneseisolatsiooninouete-kohta-euroopast-saabujatele'
page = requests.get(URL)

#get web content 

tree = html.fromstring(page.content)
update_dt = tree.xpath('//*[@id="node-article-53150"]/div[1]/div/div/div/h3[2]')
countries = tree.xpath('//*[@id="node-article-53150"]/div[1]/div/div/div/ul[3]')

#arrange webdata into a dataframe

data_dict = {
    'country': [],
    'metric': []
}

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
data_df.head()
data_df.info()

#python 3.6 f-strings
#write to disk
data_df.to_csv(f'{cur_dt}_fmin.csv')