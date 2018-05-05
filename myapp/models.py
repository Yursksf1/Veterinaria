# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

GENERO = (("M", 'Macho'), 
          ("H", 'Hembra'))

class Clinica(models.Model):
    nit         = models.CharField("Nit de la Veterinaria", max_length=20, unique=True)
    nombre      = models.CharField("Razon Social", max_length=400)
    telefono    = models.CharField("Número de teléfono", max_length=25)
    dirección   = models.CharField("Dirección", max_length=400)

    def __str__(self):
        return self.nombre

class Veterinario(models.Model):
    user                = user = models.OneToOneField(User , on_delete=models.CASCADE)
    identificacion      = models.CharField("Cédula", max_length=25, unique=True)
    targeta_profesional = models.CharField("Número de Registro", max_length=50, unique=True)
    clinica             = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class Dueño(models.Model):
    identificacion = models.CharField("Numero de identificación", max_length=20, unique=True)
    nombre         = models.CharField("Nombre del Responsable", max_length=200)
    numero         = models.CharField("Número de Contácto",max_length=25)
    telefono       = models.CharField("Teléfono Fijo", max_length=25)
    correo         = models.CharField("Correo Eletronico", max_length=500)
    direccion      = models.CharField("Dirección", max_length=500)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    dueño             = models.ForeignKey("Dueño",  on_delete=models.CASCADE)
    nombre            = models.CharField("Nombre de la Mascota", max_length=200)
    identificacion    = models.CharField("Numero de identificación", max_length=20, unique=True)
    fecha_nacimiento  = models.DateField()
    Genero            = models.CharField(default="M", choices=GENERO, max_length=1)

    def __str__(self):
        return self.nombre

class HistoriaClinica(models.Model):
    paciente    = models.ForeignKey("Paciente",  on_delete=models.CASCADE)
    veterinario = models.ForeignKey("Veterinario",  on_delete=models.CASCADE)
    clinica     = models.ForeignKey("Clinica",  on_delete=models.CASCADE)    
    descripción = models.TextField("Descripción Detallada del Proceso", max_length=200)
    fecha       = models.DateField()
    fecha_v     = models.DateField()

    def __str__(self):
        return str(self.fecha)
    
