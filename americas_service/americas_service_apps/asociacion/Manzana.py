
from uuid import uuid4
# from datetime import datetime, timedelta
from django.db import models
from django.utils.translation import ugettext_lazy as _


def validar_numero_maximo_lotes():
    pass


class Manzana(models.Model):
    """
    Clase para crear la tabla Manzana
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    manzana = models.CharField(
        _('manzana'), unique=True, max_length=3, null=False, blank=False)
    numero_lotes = models.PositiveSmallIntegerField(
        _('numero lotes'), default=1, blank=False, null=False)

    class Meta:
        verbose_name = "Manzana"
        verbose_name_plural = "Manzanas"

    def __str__(self):
        return '%s %s' % (self.manzana, self.numero_lotes)
