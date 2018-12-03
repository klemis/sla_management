from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sla_status/', views.sla_status, name='sla_status'),
    path('specific_info', views.specific_info, name='specific_info'),
]


