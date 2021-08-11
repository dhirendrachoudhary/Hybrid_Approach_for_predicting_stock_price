#Simple Moving Average (SMA)
# https://www.tradingtechnologies.com/xtrader-help/x-study/technical-indicator-definitions/simple-moving-average-sma/
# The Simple Moving Average (SMA) is calculated by adding the price of an instrument over a number of time periods and then dividing the sum by the number of time periods. The SMA is basically the average price of the given time period, with equal weighting given to the price of each period.

# Formula
# SMA = ( Sum ( Price, n ) ) / n    

# Where: n = Time Period

def SMA(dataset, n):
  # Input: dataset = pandas dataframe of historical data
  # Output: pandas dataframe with 'SMA_n' column added
  # Calculate: SMA
  dataset['SMA_' + str(n)] = dataset['Close'].transform(lambda x: x.rolling(window = n).mean())
  return dataset