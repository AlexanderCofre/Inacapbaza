from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required
from .auth import authenticate_user
from .models import Usuario
from django.contrib.auth.hashers import check_password

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
            return redirect('login')
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})

def authenticate_user(email, password):
    try:
        user = Usuario.objects.get(email=email)
        if check_password(password, user.contraseña):
            return user
    except Usuario.DoesNotExist:
        return None

def usuario_login(request):
    if request.method == 'POST':
        email = request.POST.get('correo')
        password = request.POST.get('contraseña')
        user = authenticate_user(email, password)
        if user is not None:
            login(request, user)  # Asegúrate de que `login` funcione con tu modelo
            messages.success(request, "Has iniciado sesión con éxito.")
            return redirect('inicio')
        else:
            messages.error(request, "Email o contraseña incorrectos.")
    return render(request, 'login.html')

@login_required
def usuario_logout(request):
    logout(request)
    messages.info(request, "Has cerrado sesión con éxito.")
    return redirect('inicio')
