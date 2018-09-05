from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('<str:form_id>/form', views.form, name='form')
	# path('<str:form_id>/submit', views.submit, name='submit')
	# path('<str:form_id>/info', views.edit, name='edit')
]