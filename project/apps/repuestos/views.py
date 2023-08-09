from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Mantenimiento, Servicio
from .forms import AfinacionForm, FrenosForm

class SuspencionView(FormView):
    form_class = FrenosForm
    template_name = "repuestos/suspencion.html"
    categoria_nombre = "Suspencion"
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_suspencion'] = Servicio.objects.filter(categoria__nombre=self.categoria_nombre)
        return context
    
    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios_suspencion'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)

class AfinacionView(FormView):
    form_class = AfinacionForm
    template_name = 'repuestos/afinacion.html'
    categoria_nombre = 'Afinación'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_afinacion'] = Servicio.objects.filter(categoria__nombre=self.categoria_nombre)
        return context
    
    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios_afinacion'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)

class FrenosView(FormView):
    form_class = FrenosForm
    template_name = 'repuestos/frenos.html'
    categoria_nombre = 'Frenos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_frenos'] = Servicio.objects.filter(categoria__nombre=self.categoria_nombre)
        return context
    
    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios_frenos'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)


