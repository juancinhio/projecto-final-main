from django import forms
from .models import Frenos

class FrenosForm(forms.ModelForm):
    class Meta:
        model = Frenos
        fields = ['nombre', 'cantidad', 'pedidos', 'ok']