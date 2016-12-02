from rest_framework import serializers
from americas_service_apps.asociacion.models.lote import Lote


class LoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lote
        fields = '__all__'
