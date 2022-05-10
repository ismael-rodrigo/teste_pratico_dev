from rest_framework import serializers

from api.models import ArmaModel, CalibreModel, MunicaoModel, ObjetoModel, ObjetoTipoModel


class CalibreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalibreModel
        fields = '__all__'


class ObjetoTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjetoTipoModel
        fields = '__all__'


class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjetoModel
        fields = '__all__'




class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArmaModel
        fields = '__all__'

     
class MunicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicaoModel
        fields = '__all__'
        