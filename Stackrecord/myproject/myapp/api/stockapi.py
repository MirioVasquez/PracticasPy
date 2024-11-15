import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
#url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=EG&interval=5min&apikey=6C0OCPQF36RHCMYO'
#r = requests.get(url)
#data = r.json()

#print(data)
    
import json

with open(r'C:\Users\Turtle\Desktop\Stackrecord\myproject\myapp\api\stockapi.json', 'r') as file:
    data = json.load(file)

time_series = data.get("Time Series (5min)", {})

for date, values in time_series.items():
    print(f"Date: {date}")
    print(f"Open: {values['1. open']}")
    print(f"High: {values['2. high']}")
    print(f"Low: {values['3. low']}")
    print(f"Close: {values['4. close']}")
    print(f"Volume: {values['5. volume']}")
    print("-" * 30)