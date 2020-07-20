import requests
from lxml import html
import pandas as pd

URL = 'https://vm.ee/et/teave-riikide-ja-eneseisolatsiooninouete-kohta-euroopast-saabujatele'
page = requests.get(URL)

tree = html.fromstring(page.content)
update_dt = tree.xpath('//*[@id="node-article-53150"]/div[1]/div/div/div/h3[2]')
countries = tree.xpath('//*[@id="node-article-53150"]/div[1]/div/div/div/ul[3]')

print(countries)

data_dict = {
    'country': [],
    'metric': []
}

for i in countries:
    for elem in i:
        data_dict['country'].append(elem.text_content().split()[0])
        data_dict['metric'].append(elem.text_content().split()[1])

data_df = pd.DataFrame.from_dict(data_dict)
data_df['load_dt'] = pd.to_datetime('today')
data_df.head()
data_df.info()

data_df.to_csv(r'C:\Users\raine\Documents\My Git Repositories\covid_travel_satus\2007_fmin.csv')