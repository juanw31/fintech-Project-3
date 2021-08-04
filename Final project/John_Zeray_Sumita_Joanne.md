# Dynamic Interactive Stock Dashboard
​
## Development Team
​
* Zeray Admasu - *Dashboard Constructor, Code Reviewer*
* Sumitha Prabu - *NLP -Sentiment Analysis - News Media*
* John A Kelly - *NLP - Sentiment Analysis - Social Media*
* Joanne Gates - *Deep-Learning, Time Series Analysis*
​
## About This Project
​
The purpose of this project is to create an easy-to-use interactive financial dashboard, intended for a basic, non-professional investors, with little need for tech skills to use, much like the Robinhood app.  The user can call on this dashboard to display real-time information about any SEC publicly-traded stock they are interested in. The dashboard will then output a series of impactful, easy-to-pread visuals:
​
* Historical pricing data.
* Impactful graphs and visuals of the pricing data.
* Time-series price prediction for the target stock.
* Comparative sentiment analysis (both news and social media buzz) about the target stock that could influence a buyer decision.
​
This dashboard will require the user to proivde a **stock ticker** , a **trading period** to return the historical prices covering said timeline. And the built-in python libraries will perform background data scraping and formatting into quick output graphs understandable to the user.  
​
## The Main Dashboard - Zeray Admasu
​
> insert words here. 
​
**Imports and libraries:**
* 
* 
* 
​
​
​
​
## Sentiment Analysis: News Media - Sumitha Prabu
​
> insert words here. 
​
**Imports and libaries:** 
​
​
## Sentiment Analysis: Social Media - John  A Kelly
​
* This section covers more detailed sentiment analysis involving a **social media** source as opposed to an open news source.
* Non-professional investors are overwhelmingly making decisions on emotion and FOMO-related impulses they read about on social media as opposed to objective research. 
* We decided to use **Twitter** as our social media source as we had gotten an approved Twitter developer account that provided the official Twitter API keys, and the Twitter developer portal is very user-friendly.
* When a user queries a stock in the dashboard, it will display the prioces as well as a graph visual of sentiment polarity scores of Twitter users tweeting about the company.
* When the user enterts the stock ticker in the dashboard, the program will also store that ticker into a query variable to pass to the Twitter API.
* Twitter API will scrape Twitter for recent archived tweets on the subject, clean the tweets into direct tokenzied words, and assign polarity and emotional values to those tweets, and finally return a simple plotly graph to the dashboard about people's feelings about the stock.
* So the user has price, price prediction, and sentiment about the stock to make a decision. 
​
**Imports and libaries:**
* tweepy - *pip install tweepy* - This is a library  
* textblob - *pip install textblob* - 
​
​
**STEP 1: Imports**
​
**STEP 2: Store the API keys**
​
**STEP 3: Create a Tweepy 
​
​
​
​
​
​
​
​
​
​
​
​
## Time-Series Prediction Analysis - Joanne Gates
​
> insert words here.
Collapse





Send a message to John A Kelly, Sumitha Prabhu, Zeray Admasu










