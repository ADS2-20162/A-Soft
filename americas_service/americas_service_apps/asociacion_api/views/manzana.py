from rest_framework import viewsets
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce

from ..serializers.manzana import ManzanaSerializer
from americas_service_apps.asociacion.models.manzana import Manzana


class ManzanaViewSet(viewsets.ModelViewSet):
    """
    Description: Model Description
    """
    queryset = Manzana.objects.all()
    serializer_class = ManzanaSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(id__icontains=query),
                    Q(manzana__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
