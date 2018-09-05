from django.db import models
from django.core.validators import MinValueValidator

# Patient, etc Models should go here

class Patient(models.Model):
	ID = models.IntegerField(validators=[MinValueValidator(1)])

class PersonalInfo(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
