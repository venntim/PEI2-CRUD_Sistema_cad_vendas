# Generated by Django 5.0.4 on 2024-04-27 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vendas", "0002_vendas_delete_registro_vendas"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vendas",
            old_name="situação_produto",
            new_name="situacao_produto",
        ),
    ]
