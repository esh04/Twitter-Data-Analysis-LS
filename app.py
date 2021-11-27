import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from functions import hashtags, data

# Navigation bar
nav = st.sidebar.selectbox(
    "Navigation:-", ["Overview", "Hashtag Analysis",  "Language Analysis", 'Conclusion'])

# read data
df_m=pd.read_csv("./data/translated_data.csv")
df = pd.read_csv("./data/final.csv")
# perform some manipulations
df = data(df)
hashtagList,df_h, hashtag_count = hashtags(df,df["hashtags"].explode().tolist())
language_list = ['English', 'Hindi', 'Marathi', 'Telugu', 'Tamil', 'Sindhi', 'Bengali', 'Urdu','Kannada', 'Malayalam', 'Punjabi', 'Oriya', 'Gujurati']

# OVERVIEW TAB -----------------------------------------------------------------------------------------
if nav == "Overview":
    st.title("Twitter Data Visualisation")
    st.markdown("The dashboard will visualize the different opinions of the citizens of India regarding what their National Language or Lingua Franca should be.")
    st.markdown("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, b")

# plot on a map
    st.map(df_m)
    st.markdown("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, b")

# plot a bar graph to show the most popular hashtags
    fig = px.bar(hashtag_count, y='hashtag', x='count', orientation='h' , height=1000,width=2000)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, b")

# plot a bar graph to show the most popular language scripts
    lang = df['languages'].value_counts()
    lang = lang[lang.index.isin(language_list)]
    fig2 = px.bar(lang,y = 'languages',labels={'languages':'count','index':'Language (script)'})
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, b")
    
# plot a line graph to find the trend of the tweets
    
    lang_options = st.multiselect("Select Languages (script) you wish to include in the Analysis", language_list,default=language_list[0])
    df_o = df[df['languages'].isin(lang_options)]
    fig3 = px.line(df_o, x='date', y='popularity', width=1000)
    st.plotly_chart(fig3, use_container_width=True)

    # print the top ten tweets
    top_tweets = df_o.sort_values(by='popularity', ascending=False).head(10)
    st.table(top_tweets['content'])

# --------------------------------------------------------------------------------------------------------

# HASHTAG ANALYSIS TAB ----------------------------------------------------------------------------------

elif nav == "Hashtag Analysis":
    st.title("Hashtag Analysis")
    st.markdown("Analysis of the few top hashtags Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, b")

    hashtag = st.multiselect('Select the Hashtags you wish to include in the Analysis', hashtagList, default=hashtagList[0:3])
    df_new = df_h[df_h['hashtags'].isin(hashtag)]

    lang_options2 = st.multiselect("Select Languages (script) you wish to include in the Analysis", language_list,default=language_list[0])
    df_new = df_new[df_new['languages'].isin(lang_options2)]

    # plot a line graph to find the trend of the tweets for the selected hashtags
    fig3 = px.line(df_new, x='date', y='popularity', color='hashtags',  width=1000)
    st.plotly_chart(fig3, use_container_width=True)
    top_tweets = df_new.sort_values(by='popularity', ascending=False).head(10)

    # print the top ten tweets
    st.table(top_tweets['content'])

# --------------------------------------------------------------------------------------------------------

# LANGUAGE ANALYSIS TAB ----------------------------------------------------------------------------------
elif nav == "Language Analysis":
    st.title("Language Analysis")
    st.markdown("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, b")

    lang_options3 = st.multiselect("Select Languages (script) you wish to include in the Analysis", language_list,default=language_list[1:3])
    df_o = df[df['languages'].isin(lang_options3)]

    # plot a line graph to find the trend of the tweets for the selected languages
    fig3 = px.line(df_o, x='date', y='popularity', color='languages',  width=1000)
    st.plotly_chart(fig3, use_container_width=True)
    top_tweets = df_o.sort_values(by='popularity', ascending=False).head(10)
    # print the top ten tweets
    st.table(top_tweets['content'])

    # display a wordcloud using some of the translated tweets
    st.subheader("Wordcloud")
    st.markdown("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, b")
    st.image('./data/wordcloud.png', width=500)

# --------------------------------------------------------------------------------------------------------

# CONCLUSION TAB -----------------------------------------------------------------------------------------------
elif nav == 'Conclusion':
    st.title("Conclusion")
    st.markdown("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, b")
    st.subheader("Problems Faced")

# --------------------------------------------------------------------------------------------------------