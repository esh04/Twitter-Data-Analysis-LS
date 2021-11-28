import streamlit as st
import pandas as pd
import plotly.express as px
from Pyscripts.functions import hashtags, data

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
    st.markdown("We aim to study what the diverse linguistic population of India thinks their Official Language or Lingua Franca should be.")
    st.markdown("How the attitudes, views and opinions of the public led to the backlash against Hindi as the Official Language of India and in favour of other languages.")
    st.markdown("For more detailed observations, click [here](https://github.com/esh04/Twitter-Data-Analysis-LS)")
# plot on a map
    st.subheader("Where are the users tweeting from?")
    st.map(df_m)
    st.markdown("We see that majority of the tweets are concentrated in the Southern Part of India.") 
    st.markdown("Upon further analysis, we found that most of them were backlashes against Hindi imposition and against the disparity between their respective mother tongues and Hindi.")

    st.markdown("Let us analyse the popularity of these tweets over time.")

# plot a line graph to find the trend of the tweets
    st.subheader('What are they tweeting?')
    lang_options = st.multiselect("Select Languages (script) you wish to include in the Analysis of trends", language_list,default=language_list[0])
    df_o = df[df['languages'].isin(lang_options)]
    fig3 = px.line(df_o, x='date', y='popularity', width=1000)
    st.plotly_chart(fig3, use_container_width=True)

    # print the top ten tweets
    st.markdown("Below are the ten most popular tweets following the set filter:")
    top_tweets = df_o.sort_values(by='popularity', ascending=False).head(10)
    st.table(top_tweets['content'])

# plot a bar graph to show the most popular hashtags
    st.subheader("Most Popular Hashtags")
    st.write('Below are the most popular Hashtags used by users.')
    fig = px.bar(hashtag_count.iloc[::-1], y='hashtag', x='count', orientation='h' , height=1000,width=2000)
    st.plotly_chart(fig, use_container_width=True)
    st.write('Most Indian Languages have a trending Hashtag demanding equal recognition for their regional langauge, and implentations of policies that promote it.')
    st.write('We see that one of the trending Hashtags is #Reject_Zomato. People of various linguistic backgrounds united to speak up against a statement given by a Zomato worker, discriminating against a Non-Hindi speaking customer. Read full story [here](https://indianexpress.com/article/trending/trending-in-india/zomato-chat-executives-reply-customers-complaint-7579241/)')

# plot a bar graph to show the most popular language scripts
    st.subheader("Most Popular Language Scripts")
    st.write('Below are the most popular Language scripts used by users.')
    lang = df['languages'].value_counts()
    lang = lang[lang.index.isin(language_list)]
    fig2 = px.bar(lang,y = 'languages',labels={'languages':'count','index':'Language (script)'})
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("*Note that by languages we mean only the scripts in which the tweet is written.*")
    

# --------------------------------------------------------------------------------------------------------

# HASHTAG ANALYSIS TAB ----------------------------------------------------------------------------------

elif nav == "Hashtag Analysis":
    st.title("Hashtag Analysis")

    
    st.markdown("Analysis of the few top Hashtags trending on Twitter.")

    hashtag = st.multiselect('Select the Hashtags you wish to include in the Analysis', hashtagList, default=hashtagList[0:3])
    df_new = df_h[df_h['hashtags'].isin(hashtag)]

    lang_options2 = st.multiselect("Select Languages (script) you wish to include in the Analysis", language_list,default=language_list[0])
    df_new = df_new[df_new['languages'].isin(lang_options2)]

    st.markdown('We can compare and contrast the trends followed by the various Hashtags to analyse the differences.')

    # plot a line graph to find the trend of the tweets for the selected hashtags
    fig3 = px.line(df_new, x='date', y='popularity', color='hashtags',  width=1000)
    st.plotly_chart(fig3, use_container_width=True)
    top_tweets = df_new.sort_values(by='popularity', ascending=False).head(10)
    st.markdown('*Note: Zoom into specific regions for better analysis.*')

    # print the top ten tweets
    st.markdown("Below are the ten most popular tweets following the set filter:")
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
