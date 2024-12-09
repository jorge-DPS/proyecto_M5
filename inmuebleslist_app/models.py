from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=250)
    website = models.URLField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Inmueble(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    caracteristicas = models.JSONField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="inmueble")
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.direccion

class Persona(models.Model):
    nombrePersona = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    ci = models.IntegerField()
    def __str__(self):
        return self.nombrePersona
class Interesado(models.Model):
    oferta=models.IntegerField()
    persona=models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="interesado")


