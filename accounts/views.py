#importação do forumulario ja criado pelo django para criação de novos usuarios
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form':user_form} )
                #renderizando o register.html junto com o valor de user_form

def login_view(request):
    login_form = AuthenticationForm()
    if request.method == 'POST':
        #capturado o valor de username e password e jogando para uma variavel
        username = request.POST["username"]
        password = request.POST["password"]
        #Usando o metodo de autenticação importado com isso passamos dois parametros que sao o usarname caputado acima e o password.
        user = authenticate(request, username=username, password=password)
        if user is not None: #se caso retornar algum usuario vai cair no if e vai permitir o acesso.
            login(request, user) #metodo login importado, recebe dois parametros, request e o user que utilizamos acima com o metodo authenticate e realiza o login.
            return redirect('cars_list') #redirecionando o usuario para lista de carros apos realizar o login
        else: #se caso o usuario for nulo vai cair no else e vai abrir novamente o formulario para preenchimento.
            login_form = AuthenticationForm()
    else: #request.method for get vai cair neste else.
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form':login_form})
def logout_view(request):
    logout(request)
    return redirect('cars_list')
