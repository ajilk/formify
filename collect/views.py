from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .form import PersonalInfoForm

def index(request):
	context = {'message': 'Index Page of Collect'}
	return render(request, 'collect/index.html', context)

def form(request, form_id):
	"""Should return the requested form"""
	# context = Form Data pulled from the database
	# patient = get_object_or_404(Patient, pk=1)
	form = PersonalInfoForm()
	context = { 'form': form }
	return render(request, 'forms/registration.html', context)
