from django.db import models


class MontoCuota(models.Model):

    class Meta:
        verbose_name = "MontoCuota"
        verbose_name_plural = "MontoCuotas"

    def __str__(self):
        pass
