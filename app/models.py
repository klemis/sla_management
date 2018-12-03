from django.db import models
from django.contrib import admin
# from adaptor.model import CsvModel

class Country(models.Model):
	country_name = models.CharField(max_length=100)
	def __str__(self):
		return self.country_name
	class Meta:
		verbose_name_plural = "Countries"

#TODO
# 1.Create separate class for loading csv insted od class Operator

class Operator(models.Model):
	# country = models.CharField(max_length=100)
	country = models.ForeignKey('Country', on_delete=models.CASCADE)
	operator = models.CharField(max_length=100)
	number_of_users = models.IntegerField()
	user_ok = models.IntegerField()
	user_pok = models.IntegerField()
	user_nok = models.IntegerField()
	def __str__(self):
		return self.operator
	class Meta:
		verbose_name_plural = "Operators"
