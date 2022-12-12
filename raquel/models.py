from django.db import models
from datetime import date


# Campos da entidade principal
class Principal(models.Model):
    viagem = models.CharField(max_length=100)
    data = models.DateField(default=date.today)
    remetente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    cpf_ou_cnpj_remetente = models.CharField(max_length=100)
    telefone_remetente = models.CharField(max_length=100)
    cpf_ou_cnpj_destinatario = models.CharField(max_length=100, blank=True)
    telefone_destinatario = models.CharField(max_length=100, blank=True)
    tipo_de_carga = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    taxa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default='0')
    valor_final = models.DecimalField(max_digits=10, decimal_places=2)
    frete = models.CharField(max_length=50)
    forma_pagamento = models.CharField(max_length=50)
    pagador_frete = models.CharField(max_length=50)
    descricao = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return "{} - {}".format(self.remetente, self.cpf_ou_cnpj_remetente)


# Campos da entidade produtos
class Produtos(models.Model):
    principal = models.ForeignKey(Principal, related_name='principal', on_delete=models.CASCADE)
    nf_produto = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nf_produto
