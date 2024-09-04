from django.shortcuts import render
from cars.models import Car

def Cars_views(request):
  cars = Car.objects.all().order_by('model')
  search = request.GET.get('search')
  if search:
    cars = Car.objects.filter(model__icontains = search)
  return render(request, 'cars.html',{'cars':cars } )

 