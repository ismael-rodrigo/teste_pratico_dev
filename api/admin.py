from django.contrib import admin

from api.models import ArmaModel, CalibreModel, MunicaoModel, ObjetoModel, ObjetoTipoModel

# Register your models here.


admin.site.register(ArmaModel)
admin.site.register(CalibreModel)
admin.site.register(ObjetoTipoModel)
admin.site.register(ObjetoModel)
admin.site.register(MunicaoModel)