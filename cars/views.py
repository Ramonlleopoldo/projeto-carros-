
from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView

class CarsView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    #sobrescrevendo o metodo get_queryset para aplicar filtros.
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = Car.objects.filter(model__icontains = search)
        return cars
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

class DetailCarView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class UpdateCarView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('detail_car', kwargs={'pk': self.object.pk})

    
    
class DeleteCarView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'