from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm

def cars_view(request):
  cars = Car.objects.all().order_by('model')
  search = request.GET.get('search')
  if search:
    cars = Car.objects.filter(model__icontains = search)
  return render(request, 'cars.html',{'cars':cars } )

def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        #if de verificação se os campos preenchidos foram validados conforme validações escritas no forms.
        if new_car_form.is_valid():
           #caso seja validado vai salvar, o save é uma função que escrevemos no forms.py
           new_car_form.save()
           #o retur rediceriona o usuario para lista de carros
           return redirect('cars_list')
    else:
        new_car_form = CarModelForm() #Atribuindo a função criada no forms a uma variavel.
    return render(request,'new_car.html', {'new_car_form':new_car_form})
    # requisição, template que queremos renderizar, Contexto --> conseguimos usar essa variavel no html
