from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'repuestos'

urlpatterns = [
    path("afinacion/", views.AfinacionView.as_view(), name="afinacion"),
    path("frenos/", views.FrenosView.as_view(), name="frenos"),
    path("suspencion/", views.SuspencionView.as_view(), name="suspencion"),
 
     
]

