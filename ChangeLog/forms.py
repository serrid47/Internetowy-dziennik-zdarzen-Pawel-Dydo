from django import forms

class EventForm(forms.Form):
    event_text = forms.CharField(label='Event Text', max_length=5000)