from os import error
import tweepy
from tweepy import OAuthHandler
import pandas as pd
import csv 
from secrets import get_access_key, get_access_secret, get_consumer_key, get_consumer_secret

consumer_key = get_consumer_key()
consumer_secret = get_consumer_secret()
access_key = get_access_key()
access_secret = get_access_secret()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True )

count = 1
# for tweet in tweepy.Cursor(api.search, q= "national language india OR hindi national language OR tamil national language OR national language telugu OR national language malayalam -filter:retweets", lang = "en", tweet_mode='extended').items(1000000):
for tweet in tweepy.Cursor(api.search, q= "#HindiDiwas  OR #HindiDiwas2020  OR #StopHindiImposition  OR #stopHindiImposition  OR #HindiImposition  OR #BanImposingHindi OR #BanEnglish  OR #HindiImposition  OR #StopHindiImperialism  OR #SaveRajasthani  OR #BelongsToTamilianStock  OR #2LangPolicy  OR #SindhiIsOurNationalLanguage  OR #EndHindiImposition  -filter:retweets", lang = "en", tweet_mode='extended').items(1000000):
    
     with open('data.csv', 'a') as csv_out:
        writer = csv.writer(csv_out)  # create the csv writer object
        print("here")
        try: 

            writer.writerow([count, tweet.created_at, tweet.full_text.encode('utf-8'), tweet._json['favorite_count'], tweet.retweet_count, tweet.user.location, tweet.user.followers_count, tweet.user.screen_name, tweet.user.name.encode('utf-8')])
            print(count)
            count+=1
        except tweepy.TweepError as e:
            print(e.reason)
            continue
        except StopIteration:
            break
        except error as e:
            print("Error",error)
            continue
