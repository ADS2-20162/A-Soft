from django.db import models
from americas_service_apps.auths.models.Person import Person
from americas_service_apps.auths.choices.enums import ESTADO_CIVIL_CHOICES
from americas_service_apps.auths.choices.enums import SELECT_SN_CHOICES
from americas_service_apps.socio.models.Conyuge import Conyuge


class Socio(models.Model):

    socio = models.ForeignKey(Person)
    estado_civil = models.CharField(
        max_length=20, choices=ESTADO_CIVIL_CHOICES, null=True, blank=True)
    # conyuge = models.OneToOneField(Conyuge, null=True, blank=True)
    conyuge = models.ForeignKey(Conyuge, null=True, blank=True)
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
        verbose_name = "Socio"
        verbose_name_plural = "Socios"

    def __str__(self):
        return '%s %s %s %s - (DNI: %s)' % (
            self.socio.first_name,
            self.socio.other_names,
            self.socio.last_name,
            self.socio.mother_last_name,
            self.socio.national_id_doc)
