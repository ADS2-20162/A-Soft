from uuid import uuid4
# from datetime import datetime, timedelta
from django.db import models
# from .Manzana import Manzana
from django.utils.translation import ugettext_lazy as _
# models
# from .ArregloLote import ArregloLote


class Lote(models.Model):
    """
    Clase para crear la tabla Lote
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    # manzana = models.ForeignKey(Manzana, null=False, blank=False)

    lote = models.ForeignKey(
        'self', related_name='asociacion', null=True, blank=True)
    input_lote = models.CharField(
        _('ingrese lote'), unique=True, max_length=3, null=False, blank=False)

    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"

    def __str__(self):
        return '%s' % (self.input_lote)
