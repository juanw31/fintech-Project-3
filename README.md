## DASHBOARD FOR DAY AND SWING TRADERS

Dashboard is a very useful data visualization tool. We used a python module called dash to create the dashboard. We started by creating an app called stock visualization, and then we created the layout

![Solidity Program TiereProfitSplitter](https://github.com/juanw31/fintech-Project-3/blob/main/Zeray/app.JPG)


#https://github.com/juanw31/fintech-Project-3/blob/main/Zeray/Layout.JPG
![Solidity Program TiereProfitSplitter](https://github.com/juanw31/fintech-Project-3/blob/main/Zeray/Layout.JPG)

As shown above, the layout has four inputs and one dropdown menu. The first three inputs accept text the fourth accepts only number numbers. The dropdown menu has three choices. 

![Solidity Program TiereProfitSplitter](https://github.com/juanw31/fintech-Project-3/blob/main/Zeray/CallsJPG.JPG)

After we created the layout, we specified the function of each component. As shown above, the callback function has five components as input, and the result of these five inputs/components is one output graph. 

![Solidity Program TiereProfitSplitter](https://github.com/juanw31/fintech-Project-3/blob/main/Zeray/functionJPG.JPG)

Input_data: 

    takes a stock ticker
    
period1: 

    takes the range of the data we need ( 1d, 2d , ...) d = day
    
interval1: 

    the gap between each data (1m , 5m , 10m..) m =minuet
    
MA: 

    Moving Average (it takes any number)
    

date: the drop-down menu has three choices.

    1, yesterday: it presents yesterday's performance of the input_data ticker
    
    2, the day before yesterday: it presents the performance of the selected stock two days ago.
    
    3, two days ago:  it presents the performance of the selected stock two days ago.
    



# The final look of the dashboard


![Solidity Program TiereProfitSplitter](https://github.com/juanw31/fintech-Project-3/blob/main/Zeray/MainDash.JPG)

All Five inputs are controlled. 

Row 1 , Col 1 : 

    current price for the selected symbol (example BA(The Boeing Company)

Row 2 , Col 1 : 

    The price of the selected stock one day ago. We can change this by selecting a different date from the dropdown menu


Row 1 , Col 2 : 

    Two weeks stock price for the selected stock/symbol

Row 2 , Col 2 : 

    Setiment analysis chart for the selected symbol/stock 

 1 , Col 2  and Row 2 , Col 2 shows the correlation between the price of the stocka nd the setiment analysis. 




# **Sentiment Analysis for stock news and price trend indicator**

## Steps for the sentiment analysis-price movement.

- ***BeautifulSoup Library***
    - Here BeautifulSoup library is used for webscrapping the news table from the website 'https://finviz.com/quote.ashx?t='
    ![Required_newsTable](Images/finviz_newstable.png)
    - Using inspect on the webpage we can locate table-id which is then used to scrappe tr (tablerow).
    ![tableid](Images/tableid.png)
    - The news headlines are then converted into a dataframe which is used for sentiment analysis.<p>
    

    
- ***NLTK VADER Library***
    -  NLTK VADER for sentiment analysis is used to find the neutral, postive, negative and compound sentiment for each headline. <p>
    ![Compound Values](Images/compound_values.png)

    - The compound values are then aggregated date-wise to get a meanscore dataframe.<p>
    ![meanscores](Images/mean_scores.png)

- ***Yfinance Library***
    - Yfinance is used to obtain the stock prices for the ticker and S&P500, NASDAQ, DOW30 index closing values.
    - A 2wk (week) period is considered for the price charts so that we can compare the price movements with the sentiment score. 
    - Important to remember that the **sentiment score of t0 is seen in the price movement of t1**<p>

- ***Dash Plotly Express Library***
    - Plotly express is used to create that charts for sentiment analysis and price movements.
    - Dash app is used to create a web page which can display charts on a web page and the user can interact with the chart and Dash interacts with the python code and displays the updated chart. <p>

    **Test Case A:**
    - Amazon stock was chosen to see the impact of sentiment analysis and its impact on the stock price.
    - As we can see the sentiment chart on **08/02/21 showed an uptick** and this can be seen in the **~ 1.2% increase in the stock price on 08/03/21** <p>

    ![Sentimentchart](Images/sentichart_t0.png)

    <p>

    ![AmznPriceChart](Images/amznprice_t1.png) <p>

    **Test Case B:**

    - Ford Motors stosck was chosen. 

    - News reports snapshot show that the sentiment of the news changed from negative to positive from July 24 to July 28. 

    ![Fordnews](Images/F_news.png)
    <p>


    - Ford Charts also show the price increase on July 29

    ![ford charts](Images/Ford_charts.png)
        


        # Twitter Sentiment Analysis - Elon Musk - How To Guide

* This document will the details to perform basic Twitter analsysis using the Twiiter API on accounts of interest such as, Elon Musk.
* Before we begin scraping Twitter accounts, we will first need to be approved for a Twitter developer account to get an API.

## Imports Needed

![Imports](images/Imports.PNG)

* We will need the **tweepy** library installed in our environment. It is pronoucned 'twee-py'.

> pip install tweepy

* We will also need the **text blob** library too. This will be used to visualize polarity scores of tweets and other graphs we want to make.

> pip install textblob

* We will also bring in the **os**, **dotenv**, and **load_dotenv** imports to bring in the Twtter API and secret keys.

* And any other import libraries we use for NLP functions.

## Twitter API

* In tweepy, we need to store our API keys in specific variables called **consumer_key** and **consumer_secret**

* We use **os.getenv** to read our API into the program and store in these resepctive variables.

* Twitter doesn't simply allow the API keys alone to be able to scrape Twitter data. Getting an approved developer account and API keys is the first step. Tweepy needs an access token made from these API keys. 

## Authentication and Creating an API Object

* After bringing in our .env file, storing our Twitter API credentials, we'll need an **access token** to initialize tweepy. To get this access token we need a **PIN number** provided by the Twitter developer portal.

* We need the Twitter API to get this PIN number. And the PIN number will create an access token, mapping our API credentials to the token. And we will create an API object using tweepy that will use this access token.  

### Getting the Access Token

* We will have all this code in jupyter notebook cell. This will handle authorizing and creating the tweepy API object needed to scrape tweets. 

![Authentication_Code](Tweepy_authorize.PNG)

* First we need to create a callback **uniform resource indicator** to manage data returned from the API from uncommon sources. Twitter has all kinds of data-types in tweets and posted by various sources. We will set the uri to be **oob** or out-of-band value for these purposes.

* Create an authentication object for tweepy using **OAuthHandler** and we pass in our **consumer_key**, **consumer_secret**, and **callback_uri**. We are using OAuth1.

* We store a redirect url variable. This will hold the authorzation website that we get the PIN number from.

* **webbrowser** will auto-open the redirect url instead of having to copy-paste. You will see this. Click **Authorize App** button.  In order to use this website, we need to have a Twitter developer account. 

![Authroize_Website](images/Authorize.PNG)

* A 7-digit **PIN** will appear. Copy this PIN. You'll get a new PIN every time you run the authorization cell. 

![PIN](images/PIN.PNG)

* Enter the PIN at the input prompt we coded in. Hit enter.

![Enter_PIN](images/Enter_PIN.PNG)

* You will see the access keys/token and secret token print out.

![Access](images/access_keys_2.jpg)

* **NOTE:** Your access keys will not change regardless how many times you re-run this cell and get a new PIN number. The access keys are always tied to the API keys.  

* the final line of code in this cell creates the tweepy API object itself. It will hold the access tokens. An optional parameter to pass in is **wait_on_rate_limit=True** which deals with the rate limit on API calls made to Twitter.

## Scraping Twitter

![Elon_Musk](images/elon_account.PNG)

* We need to set the user we want the API to look at. This the **@handle** on the Twitter account.

![User](images/set_user.PNG)

* Next we need to extract that accounts' timeline of tweets.

![Timeline](images/set_timeline.PNG)

* A few things to note: Twitter only permits **20** tweets per API call. And it only fetches the most current 20 tweets on the user timeline on the **current day.** This is the **rate limit** imposed by Twitter itself.

* Let's see the followers and friends count.

![Followers](images/see_followers.PNG)

* In Twitter, *followers* are people who follow the user account. Friends are who the user is following.
* We want a user with lots of followers and very few friends. A high friends number indicates the account might be a bot.
* A **blue verified checkmark** are the target accounts we want to use for business analsysis. Every government official or business brand and their corporate leaderships gets these indicators on their account.  

* Put all the raw tweets from the timeline into a DataFrame using an in-line for-loop to grab all the tweets.
* Our DataFrame will only have 1 column called **Tweets**

![DataFrame](images/dataframe.PNG)

## Cleanup

* Twitter posts contain various data types and objects that are not useful for analyzing content. We will remove these items such as @ mentions, # hastags, retweets, any non-text items. We only want tweets authored by Elon himself.

* define a function for cleaning tweets called **clean_tweets**

![Remove_Items](images/clean_tweets_.PNG)

* Our DataFrame will look cleaner. I have no figured out how to remove emoji symbols.

![Cleaned_df](images/cleaned_df.PNG)

## Subjectivity and Polarity

* **Subjectivity** analyzes and scores passed words based on their objectivity. It ranges from 0-1. Zero meaning the tweet was mostly objective. While 1 means the author was more subjective.

* **Polarity** measures and scores the emotion of the tweets such as **positive**, **negative**, and **neutral**.

* Define functions to pass in tweets and apply scoring functions on subjectivity and polarity. And we will add in columns to our DataFrame to reflect these scores.

![Subjectivity](images/subjectivity.PNG)

![Scored](images/sub_score.PNG)

* Now we need to add labels to our **polarity** scores. That is labeling them positive, negative, or neutral. We'll define a function called **senitment** to pass in a tweet and measure and label its polarity score. 
* We are only passing in the **polarity** colummn.

![Sentiment](images/polarity.PNG)

* We will have a Sentiment column

![Sentiment_2](images/sentiment.PNG)

## Save the Tweet data to a csv file

![Save_Tweets](images/save_tweets.PNG)


## Word Cloud

