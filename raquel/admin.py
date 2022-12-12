from django.contrib import admin

from .models import Principal, Produtos
from import_export.admin import ExportActionMixin


class ListandoPrincipal(ExportActionMixin, admin.ModelAdmin):
    list_display = (
        'id', 'viagem', 'data', 'remetente', 'destinatario', 'cpf_ou_cnpj_remetente', 'telefone_remetente',
        'cpf_ou_cnpj_destinatario', 'tipo_de_carga',
        'total',
        'taxa',
        'valor_final',
        'frete',
        'forma_pagamento',
        'pagador_frete')
    date_hierarchy = 'data'
    list_display_links = ('remetente', 'cpf_ou_cnpj_remetente')
    list_editable = ('frete', 'forma_pagamento', 'pagador_frete')
    search_fields = ['remetente', 'cpf_ou_cnpj_remetente', 'cpf_ou_cnpj_destinatario']
    readonly_fields = ('id',
                       'data', 'remetente',
                       'destinatario', 'cpf_ou_cnpj_remetente', 'cpf_ou_cnpj_destinatario',
                       'telefone_remetente', 'tipo_de_carga')
    list_filter = ('remetente', 'data', 'frete', 'cpf_ou_cnpj_remetente', 'cpf_ou_cnpj_destinatario')
    list_per_page = 50


class ListandoProdutos(admin.ModelAdmin):
    list_display = ('principal', 'nf_produto', 'valor')


admin.site.register(Principal, ListandoPrincipal)
admin.site.register(Produtos, ListandoProdutos)
