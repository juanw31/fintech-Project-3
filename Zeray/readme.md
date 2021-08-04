Your file to edit

Dashboard is a very useful data visualization tool. We used a python module called dash to create the dashboard. We started by creating an app called stock visualization, and then we created the layout

![Solidity Program TiereProfitSplitter](https://github.com/juanw31/fintech-Project-3/blob/main/Zeray/app.JPG)


#https://github.com/juanw31/fintech-Project-3/blob/main/Zeray/Layout.JPG
![Solidity Program TiereProfitSplitter](https://github.com/juanw31/fintech-Project-3/blob/main/Zeray/Layout.JPG)

As shown above, the layout has four inputs and one dropdown menu. The first three inputs accept text the fourth accepts only number numbers. The dropdown menu has three choices. 

![Solidity Program TiereProfitSplitter](https://github.com/juanw31/fintech-Project-3/blob/main/Zeray/CallsJPG.JPG)

After we created the layout, we will specify the function of each component. As shown above, the callback function has five components as input, and the result of these five inputs/components is one output graph. 

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




