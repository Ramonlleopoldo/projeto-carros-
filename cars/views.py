from django.shortcuts import render
from cars.models import Car

def MostrarCarro(request):
  cars = Car.objects.filter(brand__name = 'Volkswagen')
  return render(request, 'cars.html',{'cars':cars } )

 