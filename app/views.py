from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from app.models import Country, Operator


def index(request):
    return render_to_response('app/index.html')

def sla_status(request):
    return render_to_response('app/sla_status.html')

def specific_info(request):
	operator_data = Operator.objects.all();
	country_data = Country.objects.all();
	return render_to_response('app/specific_info.html', {"operator_data": operator_data})