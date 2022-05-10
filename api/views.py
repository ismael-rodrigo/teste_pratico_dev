

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

        serializer_arma = ArmaSerializer(data=request.data)
        serializer_arma.is_valid(raise_exception=True)
        novaArma = serializer_arma.create(serializer_arma.validated_data)
        novaArma.save()
        
        return Response(data=serializer_arma.data,status=status.HTTP_200_OK)

    def get(self,request):
        
        dado = ArmaModel.objects.all()
        serializer_arma = ArmaSerializer(dado,many=True)
        return Response(data=serializer_arma.data,status=status.HTTP_200_OK)




class MunicaoView(APIView):
    def post(self,request):

        serializer_municao = MunicaoSerializer(data=request.data)
        serializer_municao.is_valid(raise_exception=True)
        novaMunicao = serializer_municao.create(serializer_municao.validated_data)
        novaMunicao.save()
        
        return Response(data=serializer_municao.data,status=status.HTTP_200_OK)

    def get(self,request):
        
        dado = MunicaoModel.objects.all()
        serializer_municao = MunicaoSerializer(dado,many=True)
        return Response(data=serializer_municao.data,status=status.HTTP_200_OK)