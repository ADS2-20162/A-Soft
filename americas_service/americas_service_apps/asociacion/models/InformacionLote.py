
from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext_lazy as _

# models
# from .Lote import Lote


class InformacionLote(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    # lote = models.OneToOneField(Lote)
    area_lote = models.DecimalField(
        _('area total'), null=False, blank=False,
        decimal_places=2, max_digits=5, default=0.0)
    # area_lote = models.OneToOneField(AreaLote, null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Informacion de lote"
        verbose_name_plural = "Informacion de lotes"

    def __str__(self):
        return 'Lote: %s Area: %s' % (self.lote, self.area_lote)
