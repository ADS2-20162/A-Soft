from django.contrib import admin

from .models.Pago import Pago
from .models.Periodo import Periodo
from .models.ValidarPago import ValidarPago

admin.site.register(Pago)
admin.site.register(Periodo)
admin.site.register(ValidarPago)
