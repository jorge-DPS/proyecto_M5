from django.contrib import admin
from inmuebleslist_app.models import Inmueble, Empresa, Persona, Interesado
# Register your models here.
admin.site.register(Inmueble)
admin.site.register(Empresa)
admin.site.register(Interesado)
admin.site.register(Persona)

