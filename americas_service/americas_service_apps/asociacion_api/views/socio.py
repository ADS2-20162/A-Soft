from rest_framework import viewsets
# from django.db.models import Q
# from operator import __or__ as OR
# from functools import reduce

from ..serializers.socio import SocioSerializer
from americas_service_apps.asociacion.models.socio import Socio


class SocioViewSet(viewsets.ModelViewSet):
    """
    Description: Model Description
    """
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer

    def get_queryset(self):
        try:
            person = self.request.GET.get('person')
            if person:
                queryset = Socio.objects.filter(person__id=item)
            else:
                queryset = Socio.objects.all()

        except Exception as e:
            queryset = Socio.objects.all()

        return queryset
