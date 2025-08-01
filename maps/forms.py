from email.policy import default

from django import forms

locations = [
    ('hwy80', 'Highway 80', ),
    ('lazaretto', 'Lazaretto'),
    ('catalina', 'Catalina'),
    ('burton', 'Burton 4h',)
]

class DateForm(forms.Form):
    start = forms.DateField(label='Start Date')
    end = forms.DateField(label='End Date')
    location = forms.ChoiceField(choices=locations, label='Choose sensor location')
    csv_true = forms.BooleanField(label='Generate CSV', required=False)
    qartod_true = forms.BooleanField(label='Run QARTOD tests', required=False)
