from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UsuarioForm

def index(request):
    return render(request, 'index.html')

def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['contraseña'])
            usuario.save()

            messages.success(request, f"Usuario {usuario.nombre} creado con éxito.")
            return redirect('inicio')
    else:
        form = UsuarioForm()
    return render(request, 'register.html', {'form': form})

def usuario_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contraseña = request.POST.get('contraseña')
        usuario = authenticate(request, username=email, password=contraseña)
        if usuario is not None:
            login(request, usuario)
            messages.success(request, "Has iniciado sesión con éxito.")
            return redirect('inicio')
        else:
            messages.error(request, "Email o contraseña incorrectos.")
    return render(request, 'login.html')

def usuario_logout(request):
    logout(request)
    messages.info(request, "Has cerrado sesión con éxito.")
    return redirect('inicio')
