# Generated by Django 5.0.6 on 2024-10-06 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeAdmin', '0003_alter_venda_nacionalidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser_funcionario',
            name='token',
            field=models.CharField(max_length=8, null=True, unique=True),
        ),
    ]
