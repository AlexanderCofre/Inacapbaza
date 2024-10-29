from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UsuarioForm, CalabazaForm
from django.contrib.auth.decorators import login_required
from .auth import authenticate_user
from .models import Usuario, Calabaza
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
        print(email, password)
        user = authenticate_user(email, password)
        print(user)
        if user is not None:
            login(request, user)  # Asegúrate de que `login` funcione con tu modelo
            messages.success(request, "Has iniciado sesión con éxito.")
            print(user)
            return redirect('inicio')
        else:
            messages.error(request, "Email o contraseña incorrectos.")
    return render(request, 'login.html')

@login_required
def usuario_logout(request):
    logout(request)
    messages.info(request, "Has cerrado sesión con éxito.")
    return redirect('inicio')

def crear_calabaza(request):
    if request.method == 'POST':
        form = CalabazaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calabazas')
    else:
        form = CalabazaForm()
    
    return render(request, 'crear_calabaza.html', {'form': form})

def calabazas(request):
    calabazas = Calabaza.objects.all()
    return render(request, 'calabazas.html', {'calabazas': calabazas})

def editar_calabaza(request, calabaza_id):
    # Obtener la calabaza que se va a editar
    calabaza = get_object_or_404(Calabaza, id=calabaza_id)

    if request.method == 'POST':
        # Si el formulario fue enviado
        form = CalabazaForm(request.POST, instance=calabaza)
        if form.is_valid():
            # Guardar los cambios
            form.save()
            return redirect('calabazas')  # Cambia por la vista adecuada
    else:
        # Si es una solicitud GET, mostrar el formulario con los datos actuales
        form = CalabazaForm(instance=calabaza)

    return render(request, 'editar_calabaza.html', {'form': form, 'calabaza': calabaza})
