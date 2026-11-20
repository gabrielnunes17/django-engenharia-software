from django.shortcuts import render

def pagina_login(request):
    return render(request, 'cadastro/login.html')

def pagina_sobre(request):
    return render(request, 'cadastro/sobre.html')
