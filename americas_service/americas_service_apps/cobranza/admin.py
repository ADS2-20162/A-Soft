from django.contrib import admin
# from django.contrib.contenttypes.models import ContentType

# Register your models here.
from .models.RubroCobranza import RubroCobranza
from .models.ConceptoCobranza import ConceptoCobranza
from .models.Mora import Mora
from .models.Debe import Debe
from .models.MontoCuota import MontoCuota

admin.site.register(RubroCobranza)
admin.site.register(ConceptoCobranza)
admin.site.register(Debe)
admin.site.register(Mora)
admin.site.register(MontoCuota)
