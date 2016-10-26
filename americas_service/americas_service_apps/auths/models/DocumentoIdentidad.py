from django.db import models


class DocumentoIdentidad(models.Model):

    documento = models.CharField(
        max_length=30, unique=True, null=False, blank=False)

    class Meta:
        verbose_name = "DocumentoIdentidad"
        verbose_name_plural = "DocumentoIdentidads"

    def __str__(self):
        return '%s' % (self.documento)
