from django.db import models
from americas_service_apps.eventos.choices.enums import PAGO_INASISTENCIA_CHOICES


class Inasistencia(models.Model):

    fecha = models.DateTimeField()
    monto = models.CharField(max_length=2, choices=PAGO_INASISTENCIA_CHOICES)
    num_inasistencias = models.IntegerField()

    class Meta:
        verbose_name = "Inasistencia"
        verbose_name_plural = "Inasistencias"

    def __str__(self):
        pass
