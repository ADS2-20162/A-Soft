from django.db import models
from .Manzana import Manzana
from .Lote import Lote


class RelacionManzana(models.Model):

    manzana = models.OneToOneField(Manzana)
    lote = models.ManyToManyField(Lote)

    class Meta:
        verbose_name = "RelacionManzana"
        verbose_name_plural = "RelacionManzanas"

    def __str__(self):
        return 'Mz-%s' % (self.manzana)
