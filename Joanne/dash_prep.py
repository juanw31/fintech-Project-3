
def joa(symbol):
    
    import math
    import pandas_datareader as web
    import numpy as np
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler
    from keras.models import Sequential
    from keras.layers import Dense, LSTM
    import matplotlib.pyplot as plt
    plt.style.use('fivethirtyeight')
    import plotly.express as px

    #Get the stock quote 
    df = web.DataReader(symbol, data_source='yahoo', start='2015-07-30', end='2021-07-30') 

    #show data
    #df.tail(10)

    # get the number of rows and colums inthe data set
    #df.shape



    import plotly.express as px

  

    #Create a new dataframe with only the 'Close' column
    data = df.filter(['Close'])
    #Converting the dataframe to a numpy array
    dataset = data.values
    #Get /Compute the number of rows to train the model on
    training_data_len = math.ceil( len(dataset) *.8) # 80% training date. Math.ceil is to round up the numbers

    # Using MinMaxScaler from sklearn to scale the data betweek 0 and 1, preprocess date to fit neural network
    scaler = MinMaxScaler(feature_range = (0,1))
    scaled_data = scaler.fit_transform(dataset)

    # create the training datae set
    #create the scaled training date set
    train_data = scaled_data[0:training_data_len, :]

    #Split the data into x_train and y_train data sets
    x_train=[]
    y_train = []
    for i in range(60,len(train_data)):
        x_train.append(train_data[i-60:i,0])
        y_train.append(train_data[i,0])
        if i<= 61:
            print(x_train)
            print(y_train)
            print()


    #Convert x_train and y_train to numpy arrays
    x_train, y_train = np.array(x_train), np.array(y_train)

    #Reshape the data into the shape accepted by the LSTM
    x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))
    #x_train.shape

    #Build the LSTM network model
    model = Sequential()

    # Layer 1 
    model.add(LSTM(units=50, return_sequences=True,input_shape=(x_train.shape[1],1)))

    # Layer 2
    model.add(LSTM(units=50, return_sequences=False))

    #Output layers
    model.add(Dense(units=25))
    model.add(Dense(units=1))

    #Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Summarize the model
    #model.summary()

    # Training the model
    model.fit(x_train, y_train, batch_size = 1, epochs = 1)

    # Create the testing data set
    # Crete a new array containing scaled valueds 20% of the dataset
    test_data = scaled_data[training_data_len -60:,:]

    x_test = []
    y_test =  dataset[training_data_len : , : ] 
    
    for i in range(60,len(test_data)):
        x_test.append(test_data[i-60:i,0])

    # convert the data to a numpy array
    x_test = np.array(x_test)

    #Reshape the data into the shape accepted by the LSTM
    x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1],1))

    #Getting the models predicted price values
    predictions = model.predict(x_test) 
    predictions = scaler.inverse_transform(predictions)#Undo scaling

    # Get the root mean squrared erro(RMSE)--how accurate the model to predit the response, the standard deviatation of the residules. 
    rmse=np.sqrt(np.mean(((predictions- y_test)**2)))
    rmse

    #Plot/Create the data for the graph
    train = data[:training_data_len].copy()
    valid = data[training_data_len:].copy()
    valid['Predictions'] = predictions

    import plotly.graph_objects as go

    # Create traces
    fig = go.Figure()
    fig.add_trace(go.Line(x=train.index, y=train['Close'],
                        mode='lines',
                        name='Train'))
    fig.add_trace(go.Line(x=valid.index, y=valid['Close'],
                        mode='lines',
                        name='Val'))
    fig.add_trace(go.Line(x=valid.index, y=valid['Predictions'],
                        mode='lines',
                        name='Predictions'))
    fig.update_layout(title='Model',
                       xaxis_title='Date',
                       yaxis_title='Close Price USD ($)')
    #fig.show()
    #valid.plot()

    #fig = px.line(valid[['Close', 'Predictions']])
    #fig.show()
    return valid
    
