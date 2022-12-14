# Generated by Django 4.1.3 on 2022-12-12 15:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viagem', models.CharField(max_length=100)),
                ('data', models.DateField(default=datetime.date.today)),
                ('remetente', models.CharField(max_length=100)),
                ('destinatario', models.CharField(max_length=100)),
                ('cpf_ou_cnpj_remetente', models.CharField(max_length=100)),
                ('telefone_remetente', models.CharField(max_length=100)),
                ('cpf_ou_cnpj_destinatario', models.CharField(blank=True, max_length=100)),
                ('telefone_destinatario', models.CharField(blank=True, max_length=100)),
                ('tipo_de_carga', models.CharField(max_length=50)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('taxa', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('valor_final', models.DecimalField(decimal_places=2, max_digits=10)),
                ('frete', models.CharField(max_length=50)),
                ('forma_pagamento', models.CharField(max_length=50)),
                ('pagador_frete', models.CharField(max_length=50)),
                ('descricao', models.TextField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nf_produto', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='principal', to='raquel.principal')),
            ],
        ),
    ]
