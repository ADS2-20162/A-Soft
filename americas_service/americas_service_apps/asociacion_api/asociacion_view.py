from rest_framework import serializers, viewsets
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce

from americas_service_apps.asociacion.models.asociacion import Asociacion


class AsociacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asociacion
        fields = '__all__'


class AsociacionViewSet(viewsets.ModelViewSet):
    queryset = Asociacion.objects.all()
    serializer_class = AsociacionSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(ruc__icontains=query),
                    Q(nombre__icontains=query),
                    Q(denominacion__icontains=query),
                    Q(website__icontains=query),
                    Q(logo__icontains=query),
                    Q(created_at__icontains=query),
                    Q(update_at__icontains=query),
                    Q(cuenta_banco_id__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
