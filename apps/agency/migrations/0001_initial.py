# Generated by Django 5.1.4 on 2025-01-23 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Agencia",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "nome_contato",
                    models.CharField(max_length=101, verbose_name="nome do contato"),
                ),
                (
                    "nome_fantasia",
                    models.CharField(
                        max_length=200, verbose_name="nome fantasia da agência"
                    ),
                ),
                (
                    "email1",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="e-mail 1"
                    ),
                ),
                (
                    "email2",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="e-mail 2"
                    ),
                ),
                (
                    "email3",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="e-mail 3"
                    ),
                ),
                (
                    "telefone1",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="telefone 1"
                    ),
                ),
                (
                    "telefone2",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="telefone 2"
                    ),
                ),
                (
                    "telefone3",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="telefone 3"
                    ),
                ),
                (
                    "contato_ano",
                    models.CharField(
                        blank=True,
                        help_text="Formato: DD/MM/YYYY",
                        max_length=15,
                        null=True,
                        verbose_name="ano de contato",
                    ),
                ),
                (
                    "cnpj",
                    models.CharField(max_length=18, unique=True, verbose_name="CNPJ"),
                ),
                (
                    "cep",
                    models.CharField(
                        blank=True,
                        help_text="Formato: XXXXX-XXX",
                        max_length=9,
                        null=True,
                        verbose_name="CEP",
                    ),
                ),
                (
                    "municipio",
                    models.CharField(max_length=100, verbose_name="município"),
                ),
                ("uf", models.CharField(max_length=2, verbose_name="UF")),
                (
                    "logradouro",
                    models.CharField(
                        help_text="Rua | Avenida | Alameda | Travessa",
                        max_length=255,
                        verbose_name="logradouro",
                    ),
                ),
                ("numero", models.CharField(max_length=10, verbose_name="número")),
                (
                    "complemento",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="complemento",
                    ),
                ),
                ("bairro", models.CharField(max_length=100, verbose_name="bairro")),
                (
                    "observacao",
                    models.TextField(
                        blank=True,
                        max_length=2000,
                        null=True,
                        verbose_name="Observação",
                    ),
                ),
            ],
        ),
    ]
