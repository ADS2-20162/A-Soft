from rest_framework import serializers
from americas_service_apps.asociacion.models.manzana import Manzana


class ManzanaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manzana
        fields = '__all__'
