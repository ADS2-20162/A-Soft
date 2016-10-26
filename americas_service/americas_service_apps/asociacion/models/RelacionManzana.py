from django.db import models
from .Manzana import Manzana
from .Lote import Lote


class RelacionManzana(models.Model):

    # manzana = models.OneToOneField(Manzana)
    manzana = models.ForeignKey(Manzana)
    # lote = models.ManyToManyField(Lote)
    lote = models.OneToOneField(Lote)

    class Meta:
        verbose_name = "RelacionManzana"
        verbose_name_plural = "RelacionManzanas"

    def __str__(self):
        return 'Mz-%s Lote - %s' % (self.manzana, self.lote)
