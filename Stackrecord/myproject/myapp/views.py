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
    with open(r'C:\Users\Turtle\Desktop\Stackrecord\myproject\myapp\api\stockapi.json', 'r') as file:
        data = json.load(file)

    # Access the "Time Series (5min)" section
    time_series = data.get("Time Series (5min)", {})

    # Save each record to the database
    for date, values in time_series.items():
        Records.objects.create(
            Date_time=date,
            open=Decimal(values['1. open']),
            high=Decimal(values['2. high']),
            low=Decimal(values['3. low']),
            close=Decimal(values['4. close']),
            volume=int(values['5. volume']),
        )
    return render(request, 'stocks/success.html', {'message': 'Data loaded successfully'})

def success(request):
    Record = Records.objects.all()
    return render(request, 'stocks/success.html', {'Record': Record})

