from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm

def cars_view(request):
  cars = Car.objects.all().order_by('model')
  search = request.GET.get('search')
  if search:
    cars = Car.objects.filter(model__icontains = search)
  return render(request, 'cars.html',{'cars':cars } )

def new_car_view(request):
  new_car_form = CarForm() #Atribuindo a função criada no forms a uma variavel.
  
  return render(request,'new_car.html', {'new_car_form':new_car_form})
  #           requisição, template que queremos renderizar, Contexto --> conseguimos usar essa variavel no html