from django import forms

class ConactForm(forms.Form):
    name = forms.CharField(max_length=200)
    telephone = forms.CharField(max_length=12)

