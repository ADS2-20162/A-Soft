from django.db import models
from americas_service_apps.socio.models.SocioLote import SocioLote
from americas_service_apps.cobranza.models.Cuota import Cuota


class CuotaSocio(models.Model):

    socio = models.OneToOneField(SocioLote)
    cuota = models.ManyToManyField(Cuota)

    class Meta:
        verbose_name = "CuotaSocio"
        verbose_name_plural = "CuotaSocios"

    def __str__(self):
        return '%s %s' % (self.socio, self.cuota)
