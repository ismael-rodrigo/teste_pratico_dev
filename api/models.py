from django.db import models


## TABELA DE CALIBRE

class CalibreModel(models.Model):
    desc_calibre = models.CharField(max_length=45,verbose_name='Descrição do calibre')

    def __str__(self):
        return self.desc_calibre


## TABELA DE TIPO DE OBJETO
class Objeto_tipoModel(models.Model):
    tipo_de_objeto = models.CharField(max_length=64,verbose_name='Tipo de objeto')

    def __str__(self):
        return self.tipo_de_objeto


## TABELA DE OBJETOS
class ObjetoModel(models.Model):
    objeto_tipo_id = models.ForeignKey(Objeto_tipoModel,on_delete=models.CASCADE,verbose_name='Objeto tipo')
    def __str__(self):
        return self.objeto_tipo_id


## TABELA DE ARMAS
class ArmaModel(models.Model):
    calibre_id = models.ForeignKey(CalibreModel,on_delete=models.CASCADE ,verbose_name='Calibre')
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    quantidade_de_tiros = models.IntegerField(verbose_name='Quantidade de tiros')
    valor_estimado = models.FloatField(verbose_name='Valor estimado')
    imagem = models.ImageField()

    objeto = models.ForeignKey(ObjetoModel,on_delete=models.CASCADE,verbose_name='Objeto')

## TABELA DE MUNICAO
class MunicaoModel(models.Model):
    calibre_id = models.ForeignKey(CalibreModel,on_delete=models.CASCADE ,verbose_name='Calibre')
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    valor_estimado = models.FloatField(verbose_name='Valor estimado')
    
    objeto = models.ForeignKey(ObjetoModel,on_delete=models.CASCADE,verbose_name='Objeto')
