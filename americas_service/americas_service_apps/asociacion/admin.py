from django.contrib import admin
# from django.contrib.contenttypes.models import ContentType

# Register your models here.
from .Asociacion import Asociacion
from .Lote import Lote
from .Manzana import Manzana
# from .ArregloManzana import ArregloManzana

# admin.site.register(ContentType)

admin.site.register(Asociacion)
admin.site.register(Lote)
admin.site.register(Manzana)
# admin.site.register(ArregloManzana)
