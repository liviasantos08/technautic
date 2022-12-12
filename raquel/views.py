from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.db import transaction
from django.views.generic import CreateView
from .process import html_to_pdf
from .models import Principal
from .forms import PrincipalForm, ProdFormSet
from django.http import HttpResponse


class Base(View):
    template = 'base.html'

    def get(self, request):
        return render(request, self.template)


class FormsView(CreateView):
    model = Principal
    form_class = PrincipalForm
    template_name = 'form.html'
    success_url = reverse_lazy('base')

    def get_context_data(self, **kwargs):
        data = super(FormsView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['mercado'] = ProdFormSet(self.request.POST)
        else:
            data['mercado'] = ProdFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        mercado = context['mercado']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()

            if mercado.is_valid():
                mercado.instance = self.object
                mercado.save()
        return super(FormsView, self).form_valid(form)


class GeneratePdf(View):

    def get(self, *args, **kwargs):
        central = Principal.objects.all()
        context = {
            "central": central,
        }

        return render(self.request, 'tabela.html', context)

    def view_pdf(request, id=None):
        principal = get_object_or_404(Principal, id=id)
        produto = principal.principal.all()

        context = {
            "company": {
                "name": "Ibrahim Services",
                "address": "67542 Jeru, Chatsworth, CA 92145, US",
                "phone": "(818) XXX XXXX",
                "email": "contact@ibrahimservice.com",
            },
            "data": principal.data,
            "viagem": principal.viagem,
            "telefone_remetente": principal.telefone_remetente,
            "telefone_destinatario": principal.telefone_destinatario,
            "cpf_ou_cnpj_remetente": principal.cpf_ou_cnpj_remetente,
            "cpf_ou_cnpj_destinatario": principal.cpf_ou_cnpj_destinatario,
            "remetente": principal.remetente,
            "destinatario": principal.destinatario,
            "tipo_de_carga": principal.tipo_de_carga,
            "total": principal.total,
            "taxa": principal.taxa,
            "valor_final": principal.valor_final,
            "forma_pagamento": principal.forma_pagamento,
            "frete": principal.frete,
            "pagador_frete": principal.pagador_frete,
            "descricao": principal.descricao,
            "filho": produto,

        }

        pdf = html_to_pdf('comprovante.html', context)

        return HttpResponse(pdf, content_type='application/pdf')




