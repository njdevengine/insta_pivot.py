# every time sleep 30 sec +/- random
# every 10 sleep 300
# if you get error, take a long nap
from igramscraper.instagram import Instagram
from random import randint
from time import sleep

instagram = Instagram()

for i in range(len(unique)):
    try:
        if i % 10 == 0:
            account = instagram.get_account_by_id(unique[i])
            idf = pd.DataFrame({
            'Id': [account.identifier],
            'Username': [account.username],
            'Full name': [account.full_name],
            'Biography': [account.biography],
            'Profile pic url': [account.get_profile_picture_url()],
            'External Url': [account.external_url],
            'Number of published posts': [account.media_count],
            'Number of followers': [account.followed_by_count],
            'Number of follows': [account.follows_count],
            'Is private': [account.is_private],
            'Is verified': [account.is_verified],
            })
            idf.to_csv(r"/Users/paulalbilal/insta_scrape//"+account.username+".csv")
            print(i)
            sleep(randint(2,10)+300)
        else:
            account = instagram.get_account_by_id(unique[i])
            idf = pd.DataFrame({
            'Id': [account.identifier],
            'Username': [account.username],
            'Full name': [account.full_name],
            'Biography': [account.biography],
            'Profile pic url': [account.get_profile_picture_url()],
            'External Url': [account.external_url],
            'Number of published posts': [account.media_count],
            'Number of followers': [account.followed_by_count],
            'Number of follows': [account.follows_count],
            'Is private': [account.is_private],
            'Is verified': [account.is_verified],
            })
            idf.to_csv(r"/Users/paulalbilal/insta_scrape//"+account.username+".csv")
            sleep(randint(2,6)+10)
    except:
        print("taking a long nap... zzzZzZZZzzz")
        sleep(randint(10,20)+500)
