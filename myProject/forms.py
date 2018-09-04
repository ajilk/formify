from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=50)
    my_name = forms.CharField(label='My name', max_length=50)
