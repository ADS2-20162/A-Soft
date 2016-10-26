from django.contrib import admin

# Register your models here.
from .models.Socio import Socio
from .models.SocioLote import SocioLote
# from .models.AreaLote import AreaLote
# from .models.Email import Email

admin.site.register(Socio)
admin.site.register(SocioLote)
# admin.site.register(AreaLote)
# admin.site.register(Email)
