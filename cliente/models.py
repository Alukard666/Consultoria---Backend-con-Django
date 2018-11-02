from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Cliente(models.Model):
    nif = models.CharField(max_length=10)
    nombre = models.CharField(max_length=150, blank=True, null=True)
    apellidos = models.CharField(max_length=150, blank=True, null=True)
    dni_repres = models.CharField(max_length=10, blank=True, null=True)
    nombre_repres = models.CharField(max_length=150, blank=True, null=True)
    tlf1 = models.CharField(max_length=10, blank=True, null=True)
    tlf2 = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    poblacion = models.CharField(max_length=30, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    provincia = models.CharField(max_length=30, blank=True, null=True)
    iban = models.CharField(max_length=24, blank=True, null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.NullBooleanField)

    def save(self, *args, **kwargs):
        super(Cliente, self).save(*args, **kwargs)
