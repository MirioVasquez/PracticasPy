import json

with open(r'/Users/david/Desktop/archivos/Django/stackrecord/api/stockapi.json', 'r') as file:
    data = json.load(file)

time_series = data.get("Time Series (5min)", {})

for date, values in time_series.items():
    print(f"Timestamp: {date}")
    for key, value in values.items():
        # Remove decimal by converting to int and then to string
        display_value = value.replace('.','')
        print(f"Open: {display_value['open']}")
        print(f"High: {display_value['high']}")
        print(f"Low: {display_value['low']}")
        print(f"Close: {display_value['close']}")
        print(f"Volume: {display_value['volume']}")
        print("-" * 30)