from django.db import models

from americas_service_apps.asociacion.models.SocioLote import SocioLote
from .Evento import Evento


class Asistencia(models.Model):

    evento = models.ForeignKey(Evento)
    socio = models.ForeignKey(SocioLote)
    dni_representante = models.CharField(max_length=8, null=True, blank=True)
    fecha = models.DateTimeField()

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"

    def __str__(self):
        return '%s' % (self.socio)
