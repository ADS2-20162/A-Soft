from django.db import models
from .RubroCobranza import RubroCobranza
from americas_service_apps.socio.models.SocioLote import SocioLote
# from americas_service_apps.asociacion.models.Lote import Lote


class MontoCuota(models.Model):

    socio_lote = models.ForeignKey(SocioLote)
    # lote = models.ForeignKey(Lote)
    rubro_cobranza = models.ForeignKey(RubroCobranza)
    valor = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
    area_lote = models.DecimalField(
        decimal_places=2, max_digits=5, default=0.0)

    def save(self, *args, **kwargs):
        self.valor = self.rubro_cobranza.importe
        self.area_lote = self.socio_lote.socio_lote_id
        # self.area_lote = self.Lote.area_total
        return super(MontoCuota, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "MontoCuota"
        verbose_name_plural = "MontoCuotas"

    def __str__(self):
        # return('{0}'.format(self.valor))
        return '%s %s' % (self.socio_lote, self.valor)
