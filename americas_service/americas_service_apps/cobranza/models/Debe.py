from django.db import models
from .RubroCobranza import RubroCobranza


class Debe(models.Model):

    codigo_deb = models.AutoField(primary_key=True)
    glosa_debe = models.ForeignKey(RubroCobranza)

    class Meta:
        verbose_name = "Debe"
        verbose_name_plural = "Debes"

    def __str__(self):
        return '%s' % (self.glosa_debe.concepto_cobranza)
