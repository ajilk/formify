from django import forms

""" 
TLDR; Form is made from the model which lives in the database

These desperately needs to be converted to modelForms
because Patient and PersonalInfo for example live in the database.
It prevents repetition by not creating the form and the model seperately

""" 

class PersonalInfo(forms.Form):
	# UGLY and AWKWARD but works
	# better solutiom is widget_tweaks
	# firstname = forms.CharField(widget=forms.TextInput(attrs={'class' : ''}), label='First Name', max_length=20)

	firstname = forms.CharField(label='First Name', max_length=20)
	lastname = forms.CharField(label='Last Name', max_length=20)

# Patient will always have personal information, etc. You decide when and where 
# you want to use it.
class Patient(forms.Form):
	info = PersonalInfo()
