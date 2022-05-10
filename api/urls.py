from api.views import ArmaView, CalibreViewSet, MunicaoView, ObjetoTipoViewSet
from rest_framework.routers import DefaultRouter
from django.urls import  path

router = DefaultRouter()

router.register(r'calibres', CalibreViewSet, basename='calibres')
router.register(r'objeto-tipo', ObjetoTipoViewSet, basename='objeto-tipo')


urlpatterns = [
    path('armas', ArmaView.as_view(),name='Armas'),
    path('municao', MunicaoView.as_view(),name='Munição'),
]

urlpatterns += router.urls
    
    


