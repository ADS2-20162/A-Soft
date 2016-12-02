from django.conf.urls import url, include
from rest_framework import routers

from .views.asociacion import AsociacionViewSet
from .views.banco import CuentaBancoViewSet
from .views.person import PersonViewSet
from .views.manzana import ManzanaViewSet
from .views.lote import LoteViewSet
from .views.socio import SocioViewSet
from .views.socio_lote import SocioLoteViewSet

router = routers.DefaultRouter()

router.register(r'asociacion', AsociacionViewSet)
router.register(r'banco', CuentaBancoViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'manzanas', ManzanaViewSet)
router.register(r'lotes', LoteViewSet)
router.register(r'socios', SocioViewSet)
router.register(r'socioLotes', SocioLoteViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
