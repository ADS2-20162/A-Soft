from django.contrib import admin

from .models.Pago import Pago
from .models.Periodo import Periodo

admin.site.register(Pago)
admin.site.register(Periodo)
