from django.db import models


class TipoCuenta(models.Model):

    tipo_cuenta = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "TipoCuenta"
        verbose_name_plural = "TipoCuentas"

    def __str__(self):
        return '%s' % (self.tipo_cuenta)
