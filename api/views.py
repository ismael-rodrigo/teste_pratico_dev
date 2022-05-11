

from rest_framework import viewsets
from api.models import ArmaModel, CalibreModel, MunicaoModel, ObjetoTipoModel
from api.serializers import ArmaSerializer, CalibreSerializer, MunicaoSerializer, ObjetoTipoSerializer


class CalibreViewSet(viewsets.ModelViewSet):
    queryset = CalibreModel.objects.all()
    serializer_class = CalibreSerializer


class ObjetoTipoViewSet(viewsets.ModelViewSet):
    queryset = ObjetoTipoModel.objects.all()
    serializer_class = ObjetoTipoSerializer


class ArmaViewSet(viewsets.ModelViewSet):
    queryset = ArmaModel.objects.all()#.select_related('objeto' , 'calibre')
    serializer_class = ArmaSerializer


class MunicaoViewSet(viewsets.ModelViewSet):
    queryset = MunicaoModel.objects.all()#.select_related('objeto' , 'calibre')
    serializer_class = MunicaoSerializer
