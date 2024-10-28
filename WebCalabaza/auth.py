from django.contrib.auth.hashers import check_password
from .models import Usuario

def authenticate_user(email, password):
    try:
        user = Usuario.objects.get(email=email)
        if check_password(password, user.contraseña):  # Asegúrate de que `contraseña` esté encriptada
            return user
    except Usuario.DoesNotExist:
        return None
