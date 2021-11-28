# Twitter-Data-Analysis-LS
**Link**: https://twitter-data-analysis-ls.herokuapp.com/
#### To run the app locally:
Run `streamlit run app.py` on the terminal from the cloned repository. 

We aim to study what the diverse linguistic population of India thinks their Official Language or Lingua Franca should be. How the attitudes, views and opinions of the public led to the backlash against Hindi as the Official Language of India and in favour of other languages.

## Dataset
- Over 100000 relevent tweets, in various Indian Languages, were scraped using `snscrape`, from the years 2020-21.
- The data was cleaned, and the contents of the tweets with a valid location tag were translated to English for better understanding and analysis.

## Data Visualization
- The dashboard contains four tabs: Overview, Hashtag Analysis, Language Analysis and Conclusion.
- The Overview tab 
  - contains a map that depicts the locations most tweeted from. 
  - visualises the trend of tweets over the two years and displays the most popular tweets that were tweeted in that period.
  - presents the most popular hashtags and language scripts used where popularity is depicted by the sum of retweets and likes. 

- The Hashtag and Language Analysis tabs visualise the trends on the basis of selected Hashtags and Language scripts respectively. The latter also consists a wordcloud made from all the translated tweets in order to depict the general opinion of the public.

## Problems Faced
- **Language Identification:** As users often use the Roman alphabets instead of the languages own script (for example Devanagari for Hindi), the tool used for identifying the language failed at various instances and assigned a foreign language or undetermined language to that tweet. 
- **Sentiment Analysis:** The output recieved from the sentiment analysis (using `VADER`) needs a lot of work, as it alone cannot be used to determine anything due to the varying subject across the tweets. For example, some tweets had a negative sentiment while referring to Hindi, while some had a negative sentiment with respect to English. So the data could not be classified on the basis of their sentiments alone.
- **Translation of Tweets:** Due to the presence of more than 100000 tweets it was taking too long to run translations for all non-English tweets or was giving a too-many-requests error. So the number of tweets that were translated had to be reduced significantly. [We tried `Python-Translator`, `GoogleTranslate` and `GoSlate` for the translations.]
