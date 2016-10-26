from django.db import models


class ConceptoCobranza(models.Model):

    concepto_id = models.AutoField(primary_key=True)
    concepto_cobranza = models.CharField(
        max_length=80, unique=True, null=False, blank=False)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "ConceptoCobranza"
        verbose_name_plural = "ConceptoCobranzas"

    def __str__(self):
        return 'id - %s, Concepto - %s' % (self.concepto_id, self.concepto_cobranza)
