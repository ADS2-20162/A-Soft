from django.db import models


class Mora(models.Model):

    mora_id = models.AutoField(primary_key=True)
    concepto_mora = models.CharField(
        max_length=100, unique=True, null=False, blank=False)
    detalle_mora = models.TextField(max_length=300, null=True, blank=True)
    valor = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True, default=0.0)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Mora"
        verbose_name_plural = "Moras"

    def __str__(self):
        return 'id - %s, concepto - %s, valor - %s' % (
            self.mora_id,
            self.concepto_mora,
            self.valor)
