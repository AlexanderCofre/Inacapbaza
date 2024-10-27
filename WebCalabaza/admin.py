from django.contrib import admin
from .models import Usuario, Calabaza, Venta

# Configuración del modelo Usuario en el admin
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'email', 'telefono', 'direccion')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('nombre', 'apellido')
    ordering = ('id',)  # Orden por ID
    list_per_page = 20  # Paginación cada 20 usuarios
    fieldsets = (
        ("Información Personal", {
            'fields': ('nombre', 'apellido', 'email', 'telefono', 'direccion')
        }),
    )


# Configuración del modelo Calabaza en el admin
@admin.register(Calabaza)
class CalabazaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock')
    search_fields = ('nombre',)
    list_filter = ('precio',)
    ordering = ('id',)  # Orden por ID
    list_per_page = 20  # Paginación cada 20 calabazas
    fieldsets = (
        ("Información de la Calabaza", {
            'fields': ('nombre', 'descripcion', 'precio', 'stock')
        }),
    )


# Configuración del modelo Venta en el admin
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'calabaza', 'cantidad', 'fecha_venta', 'total')
    search_fields = ('usuario__nombre', 'calabaza__nombre')
    list_filter = ('fecha_venta',)
    ordering = ('-fecha_venta',)  # Orden de venta más reciente a la más antigua
    list_per_page = 20  # Paginación cada 20 ventas
    fieldsets = (
        ("Información de la Venta", {
            'fields': ('usuario', 'calabaza', 'cantidad', 'total')
        }),
        ("Fecha", {
            'fields': ('fecha_venta',),
            'classes': ('collapse',),  # Colapsa esta sección
        }),
    )
    readonly_fields = ('total', 'fecha_venta')  # Campos que no se pueden editar
