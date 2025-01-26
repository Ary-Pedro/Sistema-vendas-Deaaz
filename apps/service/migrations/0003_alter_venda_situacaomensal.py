# Generated by Django 5.1.4 on 2025-01-26 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venda",
            name="situacaoMensal",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Mensal", "Mensal"),
                    ("Finalizada", "Finalizada"),
                    ("Cancelada", "Cancelada"),
                ],
                default="Mensal",
                max_length=10,
                null=True,
            ),
        ),
    ]
