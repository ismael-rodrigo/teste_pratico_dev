from api.views import  ArmaViewSet, CalibreViewSet, MunicaoViewSet, ObjetoTipoViewSet
from rest_framework.routers import DefaultRouter
from django.urls import  path

router = DefaultRouter()

router.register(r'calibres', CalibreViewSet, basename='calibres')
router.register(r'objetos-tipo', ObjetoTipoViewSet, basename='objeto-tipos')
router.register(r'armas', ArmaViewSet, basename='armas')
router.register(r'municoes', MunicaoViewSet, basename='municoes')

urlpatterns = [

]

urlpatterns += router.urls
    
    


