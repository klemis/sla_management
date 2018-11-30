from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from app.models import Country, Operator


def index(request):
    # return HttpResponse("Hello, world.")
    return render_to_response('app/index.html')

def sla_status(request):
    return render_to_response('app/sla_status.html')