
from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext_lazy as _

# models
from .RelacionManzanaLote import RelacionManzanaLote


class InformacionLote(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    informacion_manzana_lote = models.OneToOneField(RelacionManzanaLote)
    area_lote = models.DecimalField(
        _('area total'), null=False, blank=False,
        decimal_places=2, max_digits=5, default=0.0)
    # area_lote = models.OneToOneField(AreaLote, null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "InformacionLote"
        verbose_name_plural = "InformacionLotes"

    def __str__(self):
        return '%s Area del Lote: %s' % (
            self.informacion_manzana_lote,
            self.area_lote)
