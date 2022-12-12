from django.forms import inlineformset_factory, NumberInput
from .custom_layout_object import *
from django import forms
from .models import Principal, Produtos
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field, Fieldset, Button, Reset

CARGA = [('minima', 'Carga minima'), ('taxa', 'Carga Com taxa')]
PAGAMENTO = [('nh', 'Nenhuma das opções'), ('dinheiro', 'Dinheiro'), ('cartao', 'Cartão'), ('pix', 'Pix')]
FRETE = [('pago', 'Pago'), ('a pagar', 'A Pagar'), ('faturado', 'Faturado')]
PAGADOR = [('nh', 'Nenhuma das opções'), ('remetente', 'Remetente'), ('destinatario', 'Destinatario')]
BARCO = [('Lancha Raquel: Belém-Barcarena', 'Lancha Raquel: Belém-Barcarena'), ('Lancha Marujo: Belém-Barcarena', 'Lancha Marujo: Belém-Barcarena')]
PESSOA = [('fisica', 'Pessoa Fisica'), ('juridica', 'Pessoa Juridica')]


class PrincipalForm(forms.ModelForm):
    viagem = forms.ChoiceField(choices=BARCO, widget=forms.RadioSelect())
    tipo_de_carga = forms.ChoiceField(choices=CARGA, widget=forms.RadioSelect())
    frete = forms.ChoiceField(choices=FRETE, widget=forms.RadioSelect())
    forma_pagamento = forms.ChoiceField(choices=PAGAMENTO, widget=forms.RadioSelect())
    pagador_frete = forms.ChoiceField(choices=PAGADOR, widget=forms.RadioSelect())

    def __init__(self, *args, **kwargs):
        super(PrincipalForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['total'].widget.attrs.update({'readonly': 'True'})
        self.helper.field_class = 'col-md-12 mb-0'
        self.helper.layout = Layout(
            Fieldset('Viagem',
                     Field('viagem'),
                     Field('data'),
                     ),
            Fieldset('Pessoa',
                     Field('remetente'),
                     Row(
                         Column('cpf_ou_cnpj_remetente', css_class='form-group col-md-6 mb-0'),
                         Column('telefone_remetente', css_class='form-group col-md-6 mb-0'),
                         css_class='form-row'
                     ),
                     Field('destinatario'),
                     Row(
                         Column('cpf_ou_cnpj_destinatario', css_class='form-group col-md-6 mb-0'),
                         Column('telefone_destinatario', css_class='form-group col-md-6 mb-0'),
                         css_class='form-row'
                     ),
                     ),
            Fieldset('Adicionar Produtos',
                     Formset('mercado')
                     ),
            Field('descricao'),
            Fieldset('Valores e Pagamento:',
                     Field('tipo_de_carga'),
                     Row(
                         Column('total', css_class='form-group col-md-3 mb-0'),
                         Column('taxa', css_class='form-group col-md-3 mb-0'),
                         Column('valor_final', css_class='form-group col-md-3 mb-0'),
                         css_class='form-row'
                     ),
                     Button('button', 'Aplicar Taxa', css_class="btn btn-danger btn-sm", onclick="getPrice()"),
                     Field('frete'),
                     Field('forma_pagamento'),
                     Field('pagador_frete'),
                     ),
            Reset('name', 'Cancelar', css_class="btn btn-primary"),
            Submit('submit', 'Salvar')

        )

    class Meta:
        model = Principal
        fields = '__all__'


class ProdFormSet(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['valor'].widget.attrs.update({'class': 'special', 'oninput': 'atualizarDinamico(this)'})
        self.helper.form_show_labels = False

    class Meta:
        model = Produtos
        fields = '__all__'


ProdFormSet = inlineformset_factory(Principal, Produtos, form=ProdFormSet,
                                    fields=['nf_produto', 'valor'],
                                    extra=1, can_delete=True)
