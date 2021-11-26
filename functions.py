from collections import Counter
from typing_extensions import final

def hashtags(df):
    df["hashtags"] = df["hashtags"].fillna('[]')
    df["hashtags"] = df["hashtags"].apply(clean)
    df["hashtags"] = df["hashtags"].str.split(" ")
    return df

def hashtags_list(hlist):
    dict =  Counter(hlist)
    final_list = [element[0] for element in dict.most_common(50)]
    return final_list

def clean(list_):
    list_ = list_.replace(' ','')
    list_ = list_.replace(',', ' ')
    list_ = list_.replace("'", '')
    list_ = list_.replace('[', '')
    list_ = list_.replace(']', '')
    return list_


