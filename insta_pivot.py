#get usernames, bios, external links from instalooter output...

from os import listdir
from os.path import isfile, join
mypath = r'mypath\#hashtag\\'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

jsons = []
for i in onlyfiles:
    if "json" in i:
        jsons.append(mypath+i)
        
import pandas as pd
data = []
for i in range(len(jsons)):
    df = pd.read_json(jsons[i]).transpose()
    data.append(df)
    
combined = pd.concat(data)
combined = combined.loc["node"]

combined.to_csv('raw_output.csv')

user_ids = []
for i in range(len(list(combined['owner']))):
    user_ids.append(list(combined['owner'])[i]['id'])

links = []
for i in list(df['owner']):
    links.append("https://i.instagram.com/api/v1/users/"+str(i)+"/info/")
    
# example: https://i.instagram.com/api/v1/users/123456.../info/
unique = list(set(user_ids))

links = []
for i in unique:
    links.append("https://i.instagram.com/api/v1/users/"+str(i)+"/info/")
    
    
    
from fake_useragent import UserAgent
import requests
from random import randint
from time import sleep

data = []
for i in links:
    with requests.Session() as s:
        ua = UserAgent()
        x = ua.random
        headers = {"user-agent" : x}
        r = s.get(i, headers=headers)
        data.append(r)
        sleep(randint(2,6))
#        print(i)

usernames = []
bios = []
external_links = []
for i in range(len(data)):
    try:
        usernames.append(data[i].json()['user']['username'])
    except:
        usernames.append(" ")
        print('username error at',i)
    try:
        bios.append(data[i].json()['user']['biography'])
    except:
        bios.append(" ")
        print('bio error at',i)
    try:
        external_links.append(data[i].json()['user']['external_url'])
    except:
        external_links.append(" ")
        print('external_link error at',i)
        
df['handle'] = usernames
df['bios'] = bios
df['external_links'] = external_links
df['link'] = ["https://www.instagram.com/"+i for i in list(df['handle'])]
df.to_csv('all_data.csv',index=False)
