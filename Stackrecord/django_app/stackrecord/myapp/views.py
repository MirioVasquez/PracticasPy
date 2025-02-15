from django.shortcuts import render, redirect
from .form import RecordForm
from .models import Records 
import json
from decimal import Decimal

# Create your views here.
def home(request):
    return render(request, 'stocks/home.html')

def add_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new record to the database
            return redirect('success')  # Redirect to a page showing all records, for example
    else:
        form = RecordForm()
    return render(request, 'stocks/add_record.html', {'form': form})

def load_json_and_save(request):
    # Load the JSON data from the file
    with open(r'/Users/david/Desktop/archivos/django_app/stackrecord/api/stockapi.json', 'r') as file:
        data = json.load(file)

    # Access the "Time Series (5min)" section
    time_series = data.get("Time Series (5min)", {})

    # Save each record to the database
    for date, values in time_series.items():
        try:
            Records.objects.create(
                Date_time=date,
                open=int((values['1. open']).replace('.','')),
                high=int((values['2. high']).replace('.','')),
                low=int((values['3. low']).replace('.','')),
                close=int((values['4. close']).replace('.','')),
                volume=int(values['5. volume']),
            )
        except Exception as e:
            print(f'Error saving records for {date}: {e}')
    return render(request, 'stocks/success.html', {'message': 'Data loaded successfully'})

def success(request):
    Record = Records.objects.all()
    return render(request, 'stocks/success.html', {'Record': Record})