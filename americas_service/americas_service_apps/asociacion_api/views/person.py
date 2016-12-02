from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from americas_service_apps.auths.choices.enums import GENDER_CHOICES
from americas_service_apps.auths.models.person import Person
from ..serializers.person import PersonSerializer


class GenderChoicesViewSet(APIView):

    def get(self, request):
        return Response(GENDER_CHOICES)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
