from django.contrib import admin

# Register your models here.
from .models.Socio import Socio
from .models.Conyuge import Conyuge

admin.site.register(Socio)
admin.site.register(Conyuge)
