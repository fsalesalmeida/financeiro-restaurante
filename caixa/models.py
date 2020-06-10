from django.db import models
from django.utils import timezone

# Create your models here.

class Caixa(models.Model):
    vl_CaixaInicial = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dt_AberturaCaixa = models.DateTimeField(default=timezone.now)
    vl_Dinheiro = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vl_CartaoCredito = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vl_CartaoDebito = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vl_Refeicao = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vl_Online = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vl_Sangria = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vl_Despesas = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vl_Entradas= models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dt_FechamentoCaixa = models.DateTimeField(default=timezone.now)

class Despesas(models.Model):
    ds_Despesa = models.CharField(max_length=255)
    vl_Despesa = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dt_Despesa = models.DateTimeField(default=timezone.now)
    tp_Despesa = models.CharField(max_length=255)

class Entradas(models.Model):
    ds_Entrada = models.CharField(max_length=50)
    vl_Entrada = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dt_Entrada = models.DateTimeField(default=timezone.now)

