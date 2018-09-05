from django import forms
from django.forms import inlineformset_factory
from .models import PersonalInfo

""" 
TLDR; Form is made from the model which lives in the database

These desperately needs to be converted to modelForms
because Patient and PersonalInfo for example live in the database.
It prevents repetition by not creating the form and the model seperately

""" 
class PersonalInfoForm(forms.ModelForm):
	class Meta:
		model = PersonalInfo
		fields = ['firstname', 'lastname']
