from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)  #  Autoincremental
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nombre_de_calle = models.CharField(max_length=50)
    numero_de_casa = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    contraseña = models.CharField(max_length=15)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def save(self, *args, **kwargs):
        if self.contraseña:
            self.set_password(self.contraseña)
        super().save(*args, **kwargs)

class Calabaza(models.Model):
    id = models.AutoField(primary_key=True)  #  Autoincremental
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)


class Venta(models.Model):
    id = models.AutoField(primary_key=True)  #  Autoincremental
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    calabaza = models.ForeignKey(Calabaza, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
