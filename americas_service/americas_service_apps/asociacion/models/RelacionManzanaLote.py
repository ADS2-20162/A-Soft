from django.db import models
from .Manzana import Manzana
from .Lote import Lote


class RelacionManzanaLote(models.Model):

    # manzana = models.OneToOneField(Manzana)
    manzana = models.ForeignKey(Manzana)
    # lote = models.ManyToManyField(Lote)
    lote = models.OneToOneField(Lote)

    class Meta:
        verbose_name = "RelacionManzanaLote"
        verbose_name_plural = "RelacionManzanaLotes"

    def __str__(self):
        return 'MZ%s-L%s' % (self.manzana, self.lote)
