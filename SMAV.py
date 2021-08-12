#Simple Moving Average Volume
def SMAV(df, n):
    """
    :param df: pandas.DataFrame
    :param n: 
    :return: pandas.DataFrame
    """
    SMA = pd.Series(df['Close'].rolling(n, min_periods=n).mean(), name='SMA_' + str(n))
    df = df.join(SMA)
    return df

