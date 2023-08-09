from django import forms
from .models import Servicio

class AfinacionForm(forms.Form):
    servicios_afinacion = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=False) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        servicios_afinacion = Servicio.objects.filter(categoria__nombre='Afinación')
        servicios_choices = [(servicio.id, servicio.nombre) for servicio in servicios_afinacion]
        self.fields['servicios_afinacion'].choices = servicios_choices

class FrenosForm(forms.Form):
    servicios_frenos = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        servicios_frenos = Servicio.objects.filter(categoria__nombre='Frenos')
        servicios_choices = [(servicio.id, servicio.nombre) for servicio in servicios_frenos]
        self.fields['servicios_frenos'].choices = servicios_choices

class SuspencionForm(forms.Form):
    servicios_frenos = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        servicios_suspencion = Servicio.objects.filter(categoria__nombre='Suspencion')
        servicios_choices = [(servicio.id, servicio.nombre) for servicio in servicios_suspencion]
        self.fields['servicios_suspencion'].choices = servicios_choices
