from django.db import models
from django.utils.translation import ugettext_lazy as _
from .Socio import Socio
from .Lote import Lote
# from .InformacionLote import InformacionLote


class SocioLote(models.Model):

    socio = models.ForeignKey(Socio)
    lote_socio = models.OneToOneField(Lote)
    # informacion_lote = models.OneToOneField(InformacionLote)
    area_construida = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0)
    estado = models.BooleanField(default=True)
    # area_lote = models.DecimalField(
    #     null=False, blank=False, decimal_places=2, max_digits=5, default=0.0)

    class Meta:
        verbose_name = "SocioLote"
        verbose_name_plural = "SocioLotes"

    def __str__(self):
        return '%s %s %s' % (
            self.socio.persona.first_name,
            self.socio.persona.documento_identidad,
            self.lote_socio.lote)
