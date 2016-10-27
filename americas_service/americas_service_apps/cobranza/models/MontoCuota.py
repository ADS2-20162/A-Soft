from django.db import models
from .RubroCobranza import RubroCobranza


class MontoCuota(models.Model):

    rub_cobr = models.ForeignKey(RubroCobranza)
    valor = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)

    def save(self, *args, **kwargs):
        self.valor = self.rub_cobr.importe
        return super(MontoCuota, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "MontoCuota"
        verbose_name_plural = "MontoCuotas"

    def __str__(self):
    	return('{0}'.format(self.valor))
