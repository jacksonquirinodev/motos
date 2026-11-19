from motorcycles.models import Motorcycle
from motorcycles.forms import MotorcycleModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class MotorcyclesListView(ListView):
    model = Motorcycle
    template_name = 'motorcycles.html'
    context_object_name = 'motorcycles'

    def get_queryset(self):
        motorcycles = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            motorcycles = motorcycles.filter(model__icontains=search)
        return motorcycles


class MotorcycleDetailView(DetailView):
    model = Motorcycle
    template_name = 'motorcycle_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewMotorcycleView(CreateView):
    model = Motorcycle
    form_class = MotorcycleModelForm
    template_name = 'new_motorcycle.html'
    success_url = '/motorcycles/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class MotorcycleUpdateView(UpdateView):
    model = Motorcycle
    form_class = MotorcycleModelForm
    template_name = 'motorcycle_update.html'

    def get_success_url(self):
        return reverse_lazy('motorcycle_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class MotorcycleDeleteView(DeleteView):
    model = Motorcycle
    template_name = 'motorcycle_delete.html'
    success_url = '/motorcycles/'
    