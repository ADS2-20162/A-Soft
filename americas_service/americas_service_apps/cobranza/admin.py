from django.contrib import admin
# from django.contrib.contenttypes.models import ContentType

# Register your models here.
from .models.RubroCobranza import RubroCobranza
from .models.ConceptoCobranza import ConceptoCobranza
from .models.Debe import Debe
from .models.Cuota import Cuota
from .models.CuotaSocio import CuotaSocio
from .models.ValidarPago import ValidarPago

admin.site.register(RubroCobranza)
admin.site.register(ConceptoCobranza)
admin.site.register(Debe)
admin.site.register(Cuota)
admin.site.register(CuotaSocio)
admin.site.register(ValidarPago)
