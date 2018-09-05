from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .form import Patient

def index(request):
	context = {'message': 'Index Page of Collect'}
	return render(request, 'collect/index.html', context)

def form(request, form_id):
	"""Returns the requested form"""
	# context = Form Data pulled from the database
	# patient = get_object_or_404(Patient, pk=1)
	patient = Patient()
	context = { 'patient': patient, 'form_id': form_id}
	return render(request, 'forms/%s.html' % form_id, context)
