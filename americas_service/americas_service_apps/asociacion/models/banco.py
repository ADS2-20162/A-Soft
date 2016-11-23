from django.db import models


class Banco(models.Model):

    banco = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"

    def __str__(self):
        return '%s' % (self.banco)
