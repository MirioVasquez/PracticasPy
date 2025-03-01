import json

with open(r'/Users/david/Desktop/Practicas_Py/PracticasPy/Stackrecord/django_app/stackrecord/api/stockapi.json', 'r') as file:
    data = json.load(file)

time_series = data.get("Time Series (5min)", {})

for date, values in time_series.items():
    print(f"Timestamp: {date}")
    print(f"Open: {values['1. open']}")
    print(f"High: {values['2. high']}")
    print(f"Low: {values['3. low']}")
    print(f"Close: {values['4. close']}")
    print(f"Volume: {values['5. volume']}")
    print("-" * 30)