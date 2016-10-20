
from uuid import uuid4
# from datetime import datetime, timedelta
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ArregloManzana(models.Model):
    """
    Clase para crear la tabla Manzana
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    arreglo_manzana = models.CharField(_('arreglo manzana'), unique=True,
                                       max_length=3, null=False, blank=False)

    class Meta:
        verbose_name = "ArregloManzana"
        verbose_name_plural = "ArregloManzanas"

    def __str__(self):
        return '%s' % (self.arreglo_manzana)
