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
        

