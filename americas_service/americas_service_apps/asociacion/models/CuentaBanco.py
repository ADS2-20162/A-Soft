# from uuid import uuid4
# from datetime import datetime
from django.db import models
# from django.utils.translation import ugettext_lazy as _
# from django.utils.text import capfirst, get_text_list


class CuentaBanco(models.Model):

    #     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    entidad_bancaria = models.CharField(
        max_length=50, unique=True, null=False, blank=False)
    tipo_cuenta = models.CharField(max_length=30, null=False, blank=False)
    numero_cuenta = models.CharField(
        max_length=50, unique=True, null=False, blank=False)

    class Meta:
        verbose_name = "CuentaBanco"
        verbose_name_plural = "CuentaBancos"

    def __str__(self):
        return '%s - (%s)' % (self.entidad_bancaria, self.numero_cuenta)
