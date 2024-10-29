# admin.py
from django.contrib import admin
from .models import Usuario, Calabaza, Venta

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'nombre_de_calle', 'numero_de_casa', 'email', 'fecha_nacimiento', 'telefono', 'contraseña')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('fecha_nacimiento',)
    ordering = ('id',)
    readonly_fields = ('id',)
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'apellido', 'nombre_de_calle', 'numero_de_casa', 'email', 'fecha_nacimiento', 'telefono', 'contraseña')
        }),
    )

@admin.register(Calabaza)
class CalabazaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio', 'stock', 'peso')
    search_fields = ('nombre',)
    list_filter = ('precio', 'stock')
    ordering = ('id',)
    readonly_fields = ('id',)
    fieldsets = (
        ('Detalles de la Calabaza', {
            'fields': ('nombre', 'descripcion', 'precio', 'stock', 'peso')
        }),
    )

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'calabaza', 'cantidad', 'fecha_venta', 'total')
    search_fields = ('usuario__nombre', 'calabaza__nombre')
    list_filter = ('fecha_venta',)
    ordering = ('id',)
    readonly_fields = ('id', 'fecha_venta', 'total')
    fieldsets = (
        ('Detalles de la Venta', {
            'fields': ('usuario', 'calabaza', 'cantidad', 'fecha_venta', 'total')
        }),
    )
