from django import forms

from .models import Money

class SpendingForm(forms.Form):
    use_date = forms.DateTimeField(label='date')
    cost = forms.IntegerField(label='cost')
    detail = forms.CharField(max_length='200',label='detail')