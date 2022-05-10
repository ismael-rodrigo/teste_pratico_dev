

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



from api.models import ArmaModel, CalibreModel, MunicaoModel, ObjetoTipoModel
from api.serializers import ArmaSerializer, CalibreSerializer, MunicaoSerializer, ObjetoSerializer, ObjetoTipoSerializer


class CalibreViewSet(viewsets.ModelViewSet):
    queryset = CalibreModel.objects.all()
    serializer_class = CalibreSerializer

class ObjetoTipoViewSet(viewsets.ModelViewSet):
    queryset = ObjetoTipoModel.objects.all()
    serializer_class = ObjetoTipoSerializer

class ArmaView(APIView):
    def post(self,request):


        try:
            objeto_tipo = ObjetoTipoModel.objects.get(tipo_de_objeto = 'arma')
            objeto_tipo_id = objeto_tipo.id
            
        except:return Response(data='Objeto tipo "arma" não encontrado',status= status.HTTP_204_NO_CONTENT)

        serializer_objeto = ObjetoSerializer(data = {"objeto_tipo":objeto_tipo_id})
        serializer_objeto.is_valid(raise_exception=True)
        serializer_objeto.save()

        dado = request.data


        dado['objeto'] = serializer_objeto.data['id']

        serializer_arma = ArmaSerializer(data=dado)
        serializer_arma.is_valid(raise_exception=True)
        serializer_arma.save()

        return Response(data=serializer_arma.data,status=status.HTTP_200_OK)

    def get(self,request):
        
        dado = ArmaModel.objects.all()
        serializer_arma = ArmaSerializer(dado,many=True)
        return Response(data=serializer_arma.data,status=status.HTTP_200_OK)




class MunicaoView(APIView):
    def post(self,request):

        try:
            objeto_tipo = ObjetoTipoModel.objects.get(tipo_de_objeto = 'munição')
            objeto_tipo_id = objeto_tipo.id
            
        except:return Response(data='Objeto tipo "munição" não encontrado',status= status.HTTP_204_NO_CONTENT)

        serializer_objeto = ObjetoSerializer(data = {"objeto_tipo":objeto_tipo_id})
        serializer_objeto.is_valid(raise_exception=True)
        serializer_objeto.save()

        dado = request.data

        dado._mutable = True
        dado['objeto'] = serializer_objeto.data['id']
        dado._mutable = False


        serializer_municao = MunicaoSerializer(data=dado)
        serializer_municao.is_valid(raise_exception=True)
        serializer_municao.save()

        return Response(data=serializer_municao.data,status=status.HTTP_200_OK)

    def get(self,request):
        
        dado = MunicaoModel.objects.all()
        serializer_municao = MunicaoSerializer(dado,many=True)
        return Response(data=serializer_municao.data,status=status.HTTP_200_OK)