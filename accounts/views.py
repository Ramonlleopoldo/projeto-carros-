#importação do forumulario ja criado pelo django para criação de novos usuarios
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('cars_list')
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form':user_form} )
                #renderizando o register.html junto com o valor de user_form


