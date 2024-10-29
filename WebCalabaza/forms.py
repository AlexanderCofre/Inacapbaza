from django import forms
from django.utils import timezone
from .models import Usuario, Calabaza

class UsuarioForm(forms.ModelForm):
    contraseña = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        max_length=15,
        label="Contraseña"
    )
    confirmar_contraseña = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar Contraseña'}),
        max_length=15,
        label="Confirmar Contraseña"
    )

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'nombre_de_calle', 'numero_de_casa', 'email', 'fecha_nacimiento', 'telefono', 'contraseña']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'nombre_de_calle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Calle'}),
            'numero_de_casa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Casa'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de Nacimiento', 'type': 'date'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
        }

    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        if len(contraseña) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return contraseña

    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get("contraseña")
        confirmar_contraseña = cleaned_data.get("confirmar_contraseña")

        if contraseña and confirmar_contraseña and contraseña != confirmar_contraseña:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        fecha_nacimiento = cleaned_data.get("fecha_nacimiento")
        if fecha_nacimiento and fecha_nacimiento > timezone.now().date():
            raise forms.ValidationError("La fecha de nacimiento no puede ser mayor a la fecha actual.")
        
        return cleaned_data


class CalabazaForm(forms.ModelForm):
    class Meta:
        model = Calabaza
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'peso']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Calabaza'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio', 'min': '1'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock Disponible'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso en gramos'}),
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None:
            if precio < 1000:
                raise forms.ValidationError("El precio debe ser mayor o igual a 1000.")
            if precio < 0:
                raise forms.ValidationError("El precio no puede ser negativo.")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock

    def clean_peso(self):
        peso = self.cleaned_data.get('peso')
        if peso is not None:
            if peso < 0:
                raise forms.ValidationError("El peso no puede ser negativo.")
            elif peso == 0:
                raise forms.ValidationError("El peso debe ser mayor a 0.")
        return peso

