# Generated by Django 4.1.3 on 2022-12-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raquel', '0002_alter_principal_taxa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principal',
            name='taxa',
            field=models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=10),
        ),
    ]
