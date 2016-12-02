from rest_framework import viewsets
# from django.db.models import Q
# from operator import __or__ as OR
# from functools import reduce

from ..serializers.lote import LoteSerializer
from americas_service_apps.asociacion.models.lote import Lote


class LoteViewSet(viewsets.ModelViewSet):
    """
    Description: Model Description
    """
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer

    def get_queryset(self):
        try:
            manzana = self.request.GET.get('manazana')
            if manzana:
                queryset = Lote.objects.filter(manzana__id=item)
            else:
                queryset = Lote.objects.all()

        except Exception as e:
            queryset = Lote.objects.all()

        return queryset
