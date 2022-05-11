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
    objeto = ObjetoSerializer(read_only = True)

    def create(self,validated_data):
        print(validated_data)
        tipoArma = ObjetoTipoModel.objects.get(tipo_de_objeto = 'arma')
        objeto = ObjetoModel(objeto_tipo = tipoArma)
        objeto.save()
        
        return ArmaModel.objects.create(objeto=objeto , **validated_data)


    class Meta:
        model = ArmaModel
        fields = '__all__'
        read_only_fields = ['objeto']




class MunicaoSerializer(serializers.ModelSerializer):
    objeto = ObjetoSerializer(read_only = True)


    def create(self,validated_data):
        tipoMunicao = ObjetoTipoModel.objects.get(tipo_de_objeto = 'munição')
        objeto = ObjetoModel(objeto_tipo = tipoMunicao)
        objeto.save()
        
        return MunicaoModel.objects.create(objeto=objeto , **validated_data)



    class Meta:
        model = MunicaoModel
        fields = '__all__'
        read_only_fields = ['objeto']