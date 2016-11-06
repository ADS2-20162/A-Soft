from django.contrib import admin
# from django.contrib.contenttypes.models import ContentType

# Register your models here.
from .models.Asociacion import Asociacion
from .models.Lote import Lote
from .models.Manzana import Manzana
from .models.CuentaBanco import CuentaBanco
# from .models.InformacionLote import InformacionLote
from .models.Socio import Socio
from .models.SocioLote import SocioLote
# from .models.Banco import Banco
# from .models.TipoCuenta import TipoCuenta

# admin.site.register(ContentType)


class LoteInline(admin.TabularInline):
    model = Lote
    extra = 1


class ManzanaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['manzana']}), ]
    inlines = [LoteInline]

admin.site.register(Asociacion)
admin.site.register(Lote)
admin.site.register(Manzana, ManzanaAdmin)
# admin.site.register(ManzanaLote)
admin.site.register(CuentaBanco)
# admin.site.register(RelacionManzanaLote, RelacionManzanaLoteAdmin)
# admin.site.register(RelacionManzanaLote)
# admin.site.register(InformacionLote)
admin.site.register(Socio)
admin.site.register(SocioLote)
# admin.site.register(Banco)
# admin.site.register(TipoCuenta)
