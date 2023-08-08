from django.urls import path
from django.views.generic import TemplateView
from .views import FrenosForm

app_name = 'repuestos'

urlpatterns = [
      path('', FrenosForm.as_view(), name='crear_frenos'),
     
]

