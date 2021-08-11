def getdata(ticker, start_date, end_date):
  dataset = pd.DataFrame()
  try:
      data = pdr.get_data_yahoo(ticker, start = start_date, end = end_date)
      dataset = dataset.append(data)
  except:
      print("Data not found for ticker: " + ticker)
  return dataset