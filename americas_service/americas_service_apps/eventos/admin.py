from django.contrib import admin
from .models.Asistencia import Asistencia
from .models.Evento import Evento
from .models.Inasistencia import Inasistencia
# Register your models here.

admin.site.register(Asistencia)
admin.site.register(Evento)
admin.site.register(Inasistencia)
