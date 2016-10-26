from django.db import models
from django.utils.translation import ugettext_lazy as _
# from americas_service_apps.asociacion.models.Lote import Lote


class AreaLote(models.Model):

    area_construida = models.DecimalField(
        _('area construida'), null=False, blank=False,
        decimal_places=2, max_digits=5)
    area_sin_construir = models.DecimalField(
        _('area sin construir'), null=False, blank=False,
        decimal_places=2, max_digits=5)
    # imagen = models.ImageField()
    observaciones = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "AreaLote"
        verbose_name_plural = "AreaLotes"

    def __str__(self):
        return '%s' % (self.area_construida)
