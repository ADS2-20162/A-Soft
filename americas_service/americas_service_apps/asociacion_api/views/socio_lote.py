from rest_framework import viewsets
# from django.db.models import Q
# from operator import __or__ as OR
# from functools import reduce

from ..serializers.socio_lote import SocioLoteSerializer
from americas_service_apps.asociacion.models.socio_lote import SocioLote
from americas_service_apps.asociacion.models.lote import Lote


class SocioLoteViewSet(viewsets.ModelViewSet):
    """
    Description: Model Description
    """
    queryset = SocioLote.objects.all()
    queryset = Lote.objects.all()
    serializer_class = SocioLoteSerializer

    def get_queryset(self):
        try:
            socio = self.request.GET.get('socio')
            lote = self.request.GET.get('lote')
            if socio:
                queryset = Socio.objects.filter(socio__id=item)
                queryset = Lote.objects.filter(lote__id=item)
            else:
                queryset = SocioLote.objects.all()

        except Exception as e:
            queryset = SocioLote.objects.all()

        return queryset
