
from uuid import uuid4
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Lote(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    codigo_lote = models.CharField(
        _('arreglo lote'), unique=True, max_length=2, null=False)
    area_total = models.DecimalField(
        _('area total'), null=False, blank=False, decimal_places=2, max_digits=5)
    area_construida = models.DecimalField(
        _('area construida'), null=False, blank=False, decimal_places=2, max_digits=5)
    area_sin_construir = models.DecimalField(
        _('area sin construir'), null=False, blank=False, decimal_places=2, max_digits=5)
    # imagen = models.ImageField()
    observaciones = models.TextField(max_length=500)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"

    def __str__(self):
        return '%s %s' % (self.id, self.codigo_lote, self.area_total)
