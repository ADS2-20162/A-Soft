from django.conf.urls import url, include
from rest_framework import routers

from .views.asociacion import AsociacionViewSet

router = routers.DefaultRouter()

router.register(r'asociacion', AsociacionViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
