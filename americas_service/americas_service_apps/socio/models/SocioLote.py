from django.db import models
from django.utils.translation import ugettext_lazy as _
from americas_service_apps.socio.models.Socio import Socio
from americas_service_apps.asociacion.models.RelacionManzana import RelacionManzana


class SocioLote(models.Model):

    socio = models.ForeignKey(Socio)
    socio_lote = models.OneToOneField(RelacionManzana)

    class Meta:
        verbose_name = "SocioLote"
        verbose_name_plural = "SocioLotes"

    def __str__(self):
        return '%s %s Mz-%s L-%s' % (
            self.socio.persona.first_name,
            self.socio.persona.documento,
            self.socio_lote.manzana,
            self.socio_lote.lote)
