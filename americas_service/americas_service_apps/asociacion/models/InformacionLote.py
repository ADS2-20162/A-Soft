
from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext_lazy as _

# models
from .Lote import Lote


class InformacionLote(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    informacion_lote = models.OneToOneField(Lote)
    area_lote = models.DecimalField(
        _('area total'), null=False, blank=False,
        decimal_places=2, max_digits=5, default=0.0)
    # area_lote = models.OneToOneField(AreaLote, null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "InformacionLote"
        verbose_name_plural = "InformacionLotes"

    def __str__(self):
        return 'Area del Lote: %s' % (self.area_lote)
