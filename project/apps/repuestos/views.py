from django.views.generic.edit import FormView
from .forms import FrenosForm
from django.urls import reverse_lazy
from .models import Frenos

class FrenosForm(FormView):
    template_name = 'repuestos/repuestos.html'
    form_class = FrenosForm
    success_url = reverse_lazy('home:home')  # Cambia esta URL a la que deseas redirigir después de enviar el formulario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        default_nombres = Frenos.get_default_nombres()
        context['default_nombres'] = default_nombres
        return context

