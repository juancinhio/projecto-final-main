from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Mantenimiento, Servicio
from .forms import AfinacionForm, FrenosForm, SuspencionForm

from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import AfinacionForm
from .forms import FrenosForm
from .forms import SuspensionForm
from .models import Mantenimiento, Servicio

class AfinacionView(FormView):
    form_class = AfinacionForm
    template_name = 'repuestos/afinacion.html'
    categoria_nombre = 'Afinación'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)

class FrenosView(FormView):
    form_class = FrenosForm
    template_name = 'repuestos/frenos.html'
    categoria_nombre = 'Frenos'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)

class SuspensionView(FormView):
    form_class = SuspensionForm
    template_name = 'repuestos/suspension.html'
    categoria_nombre = 'Suspensión'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)