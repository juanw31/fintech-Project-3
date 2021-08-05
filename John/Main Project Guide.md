# Dynamic Interactive Stock Dashboard

## Development Team

* Zeray Admasu - *Dashboard Constructor, Code Reviewer*
* Sumitha Prabu - *NLP -Sentiment Analysis - News Media*
* John A Kelly - *NLP - Sentiment Analysis - Social Media*
* Joanne Gates - *Deep-Learning, Time Series Analysis*

## About This Project

The purpose of this project is to create an easy-to-use interactive financial dashboard, intended for a basic, non-professional investors, with little need for tech skills to use, much like the Robinhood app.  The user can call on this dashboard to display real-time information about any SEC publicly-traded stock they are interested in. The dashboard will then output a series of impactful, easy-to-pread visuals:

* Historical pricing data.
* Impactful graphs and visuals of the pricing data.
* Time-series price prediction for the target stock.
* Comparative sentiment analysis (both news and social media buzz) about the target stock that could influence a buyer decision.

This dashboard will require the user to proivde a **stock ticker** , a **trading period** to return the historical prices covering said timeline. And the built-in python libraries will perform background data scraping and formatting into quick output graphs understandable to the user.  

## The Main Dashboard - Zeray Admasu

> insert words here. 

**Imports and libraries:**
* 
* 
* 




## Sentiment Analysis: News Media - Sumitha Prabu

> insert words here. 

**Imports and libaries:** 


## Sentiment Analysis: Social Media - John  A Kelly

* This section covers more detailed sentiment analysis involving a **social media** source as opposed to an open news source.
* Non-professional investors are overwhelmingly making decisions on emotion and FOMO-related impulses they read about on social media as opposed to objective research. 
* We decided to use **Twitter** as our social media source as we had gotten an approved Twitter developer account that provided the official Twitter API keys, and the Twitter developer portal is very user-friendly.
* When a user queries a stock in the dashboard, it will display the prioces as well as a graph visual of sentiment polarity scores of Twitter users tweeting about the company.
* When the user enterts the stock ticker in the dashboard, the program will also store that ticker into a query variable to pass to the Twitter API.
* Twitter API will scrape Twitter for recent archived tweets on the subject, clean the tweets into direct tokenzied words, and assign polarity and emotional values to those tweets, and finally return a simple plotly graph to the dashboard about people's feelings about the stock.
* So the user has price, price prediction, and sentiment about the stock to make a decision. 

**Imports and libaries:**

* tweepy - *pip install tweepy* - This is a library that interacts with Twitter API to scrape raw tweets data from the platform. 
* textblob - *pip install textblob* - This will allow us create visuals of tokenized words and sentences of the tweets we collect into categorial segments.
* os, dotenv, and load_dotenv - to bring in our API keys securely into the main program.
* Standard NLP libraries like nltk.
* wordcloud & pillow - build wordclouds with the tweets sentiment. 
* webbrowser and time - these are somewhat standard libraries and do not really require a stand alone. These will redirect users to Twitter authorization url to get our **access token** with our Twitter API keys. 
* matplotlib
* plotly express
* pandas - to make our dataframes.
* re - to replace and substitue unwanted Twitter elements out of the data when data cleaning. 

**Limitations:**

* To do this section, you need **Twitter API keys** which can only be obtained by having an **approved Twitter developer account.** 
* The Twitter API keys alone will not allow data scraping. Any app or code notebook will require an access token using the API keys.
* Tweepy will use the access token to scrape the data.
* You are only permitted 500,000 tweets per day. 
* API is **rate limited** to **20 tweets** per API call for @Twitter handlles.
* You can get more tweets data if we search by a #hashtag subject, using the but this will require extra code to pull the tweets data, and extra cleanup code to streamline the text data.
* The tweepy **Cursor** function will be able to collect more tweets.
* You can only get the past **5-7 days worth of recent** tweet data on a subject.
* Multiple API calls can trigger a rate-limit issue or a token authorization issue. To fix this you'll need to go back into the Twitter developer portal and regenerate new API credentials and update your environment variables.

**STEP 1: Imports**

![Imports](Images/Imports.PNG)

* We will need the **tweepy** library installed in our environment. It is pronoucned 'twee-py'.

> pip install tweepy

* We will also need the **text blob** library too. This will be used to visualize polarity scores of tweets and other graphs we want to make.

> pip install textblob

* We will also bring in the **os**, **dotenv**, and **load_dotenv** imports to bring in the Twtter API and secret keys.

* And any other import libraries we use for NLP functions.


**STEP 2: Store the API keys**

* In tweepy, we need to store our API keys in specific variables called **consumer_key** and **consumer_secret**

* We use **os.getenv** to read our API into the program and store in these resepctive variables.

* Twitter doesn't simply allow the API keys alone to be able to scrape Twitter data. Getting an approved developer account and API keys is the first step. Tweepy needs an access token made from these API keys.


**STEP 3: Create a Tweepy API Object to scrape Twitter**

* After bringing in our .env file, storing our Twitter API credentials, we'll need an **access token** to initialize tweepy. To get this access token we need a **PIN number** provided by the Twitter developer portal.

* We need the Twitter API to get this PIN number. And the PIN number will create an access token, mapping our API credentials to the token. And we will create an API object using tweepy that will use this access token.  
* We will have all this code in jupyter notebook cell. This will handle authorizing and creating the tweepy API object needed to scrape tweets. 

![Authentication_Code](Images/Tweepy_authorize.PNG)

* First we need to create a callback **uniform resource indicator** to manage data returned from the API from uncommon sources. Twitter has all kinds of data-types in tweets and posted by various sources. We will set the uri to be **oob** or out-of-band value for these purposes.

* Create an authentication object for tweepy using **OAuthHandler** and we pass in our **consumer_key**, **consumer_secret**, and **callback_uri**. We are using OAuth1.

* We store a redirect url variable. This will hold the authorzation website that we get the PIN number from.

* **webbrowser** will auto-open the redirect url instead of having to copy-paste. You will see this. Click **Authorize App** button.  In order to use this website, we need to have a Twitter developer account. 

![Authroize_Website](Images/Authorize.PNG)

* A 7-digit **PIN** will appear. Copy this PIN. You'll get a new PIN every time you run the authorization cell. 

![PIN](Images/PIN.PNG)

* Enter the PIN at the input prompt we coded in. Hit enter.

![Enter_PIN](Images/Enter_PIN.PNG)

* You will see the access keys/token and secret token print out.

![Access](Images/access_keys_2.jpg)

* **NOTE:** Your access keys will not change regardless how many times you re-run this cell and get a new PIN number. The access keys are always tied to the API keys.  

* the final line of code in this cell creates the tweepy API object itself. It will hold the access tokens. An optional parameter to pass in is **wait_on_rate_limit=True** which deals with the rate limit on API calls made to Twitter.

**STEP 4: DataFrame of Tweets**

* We will scrape 1000 tweets and put into a pandas DataFrame

* This dataframe will have 1 column called **Tweets**

* Define our search topic by declaring a variable and storing a '#hashtag' I chose dogecoin

![DataFrame](Images/make_dataframe.png)

**STEP 5: CLeanup**

* We want to get rid of all unecessary tweet elements like emoji's, videos, images, ASCII art.
* We want sentiment from organic authored tweets. Clean up re-tweets, ads, and spam.

* Define an emoji script. This will be used.

![Emojis](Images/emoji_reference.png)

* Define a **clean_tweets** function to substitue out all unwanted emoji's and data-types

![Cleanup](Images/clean_tweets.png)

**STEP 6: Subjectivity and Polarity** 

* Subjectivity measures the emotional tone of a tweet whether it's objective or subjective. It ranges from 0-1. Zero is objective and 1 is subjective. 

* Define both a subjectivity and polarity functions to apply new columns and scores of each tweet collected.

![Scoring](Images/sub_pol.png)

* Add sentiment labels to the polarity scores with **positive**, **negative**, and **neutral** labels.

![Sentiment](Images/sentiment2.png)

* Final cleaned up tweets dataframe

![Cleaned](Images/final_dataframe.png)

**STEP 6: Visualize the Sentiment in Graphs and Word Cloud**

* Make a scatterplot

![Scatterplot](Images/scatterplot.png)

* Make a plotly express pie chart

![Pie_Chart](Images/pie_chart.png)

* Make a word cloud

![WC_Code](Images/wordcloud_code.png)

![WC](Images/wordcloud.png)

## Time-Series Prediction Analysis - Joanne Gates

> insert words here.