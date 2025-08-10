from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import  HttpResponse
from django.contrib.messages import constants
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your views here.
def  cadastro(request):
    if request.method == 'GET': 
        # se o metdo for GET, renderiza o template cadastro.html
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        #Se o Metodo for POST ele pega as informações do formulario
       
        nome= request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get ('telefone')
        provincia = request.POST.get('provincia')
        distrito = request.POST.get ('distrito')
        apelido = request.POST.get('apelido')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
       

        if (len(senha) < 6):
            messages.add_message(request, constants.ERROR, 'Palavra-passe deve ter no minimo 6 caracteres' )
            
            return redirect ('cadastro')
        if ( not senha == confirmar_senha):
            messages.add_message(request, constants.ERROR, 'As senhas sao diferentes' )
            return redirect('cadastro')
        
        #Busca o usuario na base de dados
        usuario = CustomUser.objects.filter(email= email )
        
        
        #verifica se o usuario existe ou nao!
        if (usuario.exists()):
            messages.add_message(request,constants.ERROR, 'Esse nome de usuario existe')
            return redirect('cadastro')
        
       
        
        user = CustomUser.objects.create_user(
            
           
            password=senha,
            email=email,
            nome=nome,
            apelido=apelido,
            telefone=telefone,
            provincia=provincia,
            distrito=distrito
            
        )
            
        
     
        
        
    return HttpResponse(  'Cadastro feito com sucesso')

def login_view(request):
   if request.method == 'GET':
       return render(request,'login.html')
   elif request.method == 'POST':
       email=request.POST.get('email')
       password=request.POST.get('senha')
       
       user = authenticate(request, email=email,password=password)
       
       if user:
           login(request,user)
           return HttpResponse("Login feito com sucesso")
       messages.add_message(request, constants.ERROR, 'Email ou senha invalidos')
       return redirect('login')
 
def logout_view (request):
    logout(request)
    return redirect ("login") 