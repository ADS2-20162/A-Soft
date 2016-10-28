from django.db import models
from .RubroCobranza import RubroCobranza
from americas_service_apps.asociacion.models.InformacionLote import InformacionLote


class Cuota(models.Model):

    lote = models.ForeignKey(InformacionLote)
    rubro_cobranza = models.ForeignKey(RubroCobranza)
    valor = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
    area_lote = models.DecimalField(
        decimal_places=2, max_digits=5, default=0.0)
    cuota = models.DecimalField(
        decimal_places=2, max_digits=5, default=0.0)

    def save(self, *args, **kwargs):
        self.valor = self.rubro_cobranza.importe
        self.area_lote = self.lote.area_lote
        self.cuota = self.valor * self.area_lote
        return super(Cuota, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Cuota"
        verbose_name_plural = "Cuotas"

    def __str__(self):
        # return('{0}'.format(self.valor))
        return '%s %s Cuota: %s' % (self.lote, self.valor, self.cuota)
