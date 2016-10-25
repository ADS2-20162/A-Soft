from django.db import models
from americas_service_apps.auths.models.Person import Person
from americas_service_apps.auths.choices.enums import SELECT_SN_CHOICES
# from americas_service_apps.auths.choices.enums import ESTADO_CIVIL_CHOICES


class Conyuge(models.Model):

    conyuge = models.ForeignKey(Person)
    # conyuge = models.OneToOneField(Conyuge, null=True, blank=True)
    domicilio = models.CharField(max_length=300, null=True, blank=True)
    procedencia = models.CharField(max_length=50, null=True, blank=True)
    celular = models.CharField(max_length=30, null=True, blank=True)
    telefono = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    residencia_juliaca = models.CharField(
        max_length=2, choices=SELECT_SN_CHOICES)
    is_adventista = models.CharField(
        max_length=2, choices=SELECT_SN_CHOICES)

    class Meta:
        verbose_name = "Conyuge"
        verbose_name_plural = "Conyuges"

    def __str__(self):
        return '%s - %s' % (self.conyuge.first_name,
                            self.conyuge.national_id_doc)
