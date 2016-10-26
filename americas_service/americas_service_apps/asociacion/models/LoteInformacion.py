
from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext_lazy as _
# models
# from .Manzana import Manzana
from .RelacionManzana import RelacionManzana
# from .Lote import Lote
from .AreaLote import AreaLote


class LoteInformacion(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    manzana = models.ForeignKey(RelacionManzana)
    # lote = models.OneToOneField(Lote)
    # codigo_lote = models.CharField(
    #     _('arreglo lote'), unique=True, max_length=2, null=False)
    area_total = models.DecimalField(
        _('area total'), null=False, blank=False,
        decimal_places=2, max_digits=5, default=0.0)
    area_lote = models.OneToOneField(AreaLote, null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "LoteInformacion"
        verbose_name_plural = "LoteInformacions"

    def __str__(self):
        return 'Mz-%s Lote-%s' % (self.manzana, self.lote)
