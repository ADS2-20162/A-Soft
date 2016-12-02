from rest_framework import serializers
from americas_service_apps.asociacion.models.socio_lote import SocioLote
# from americas_service_apps.auths.choices.enums import GENDER_CHOICES


class SocioLoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocioLote
        fields = '__all__'
