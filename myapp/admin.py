from django.contrib import admin

# Register your models here.
from .models import Clinica, Veterinario, Dueño, Paciente, HistoriaClinica




class ClinicaAdmin(admin.ModelAdmin):
    list_display = ('nit', 'nombre', 'telefono', 'dirección' )
    search_fields = ['nit', 'nombre', 'telefono', 'dirección']


class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'identificacion', 'targeta_profesional')
    search_fields = ['user','identificacion']

class DueñoAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'nombre', 'correo', 'numero' )
    search_fields = ['identificacion']


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'nombre', 'Genero')
    list_filter = ['Genero']
    search_fields = ['identificacion','nombre']


class HistoriaClinicaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'veterinario', 'fecha')

admin.site.register(Clinica, ClinicaAdmin)
admin.site.register(Veterinario, VeterinarioAdmin)
admin.site.register(Dueño,DueñoAdmin)
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(HistoriaClinica, HistoriaClinicaAdmin)