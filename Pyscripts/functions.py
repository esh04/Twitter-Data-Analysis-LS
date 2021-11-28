from collections import Counter
from typing_extensions import final
import pandas as pd

# some data manipulations
def data(df):
    df["hashtags"] = df["hashtags"].fillna('[]')
    df["hashtags"] = df["hashtags"].apply(clean)
    df["hashtags"] = df["hashtags"].str.split(" ")
    # defines popularity of a tweet
    df["popularity"] = df["likeCount"] + df["retweetCount"]
    return df

def hashtags(df, hlist):
    
    # Count the number of hashtags in the data
    dict =  Counter(hlist)
    # Create a dataframe using the top 50 tweets
    new_dict = dict.most_common(50)
    final_list = [element[0] for element in new_dict]
    # remove irrelevant hashtags
    final_list.remove('म')
    hashtag_count = pd.DataFrame.from_records(new_dict, columns =['hashtag', 'count'])

    # create a new dataframe by exploding the hashtags lists column
    df = df.explode('hashtags')
    df = df[df['hashtags'].isin(final_list)]

    return final_list,df, hashtag_count

# Clean the hashtags column of the data
def clean(list_):
    list_ = list_.replace(' ','')
    list_ = list_.replace(',', ' ')
    list_ = list_.replace("'", '')
    list_ = list_.replace('[', '')
    list_ = list_.replace(']', '')
    return list_


