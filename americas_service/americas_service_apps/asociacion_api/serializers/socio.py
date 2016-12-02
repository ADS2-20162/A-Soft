from rest_framework import serializers
from americas_service_apps.asociacion.models.socio import Socio
# from americas_service_apps.auths.choices.enums import GENDER_CHOICES


class SocioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Socio
        fields = '__all__'
