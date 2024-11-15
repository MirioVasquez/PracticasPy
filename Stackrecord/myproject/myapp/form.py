from django import forms
from .models import Records

class RecordForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['Date_time', 'open', 'high', 'low', 'close', 'volume']