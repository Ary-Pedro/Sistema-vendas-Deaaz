# Generated by Django 5.0.6 on 2024-09-29 14:11

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Digite o nome aqui.', max_length=100, verbose_name='Nome')),
                ('celular', models.CharField(help_text='Digite seu Telefone aqui. como no exemplo: (21) 9xxxx-xxxx', max_length=15, verbose_name='Celular')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Sexo')),
                ('data_nascimento', models.DateField(help_text='Data de nascimento', verbose_name='Data de nascimento')),
                ('endereco', models.CharField(blank=True, help_text='Digite a endereço aqui.', max_length=200, null=True, verbose_name='Endereço')),
                ('bairro', models.CharField(blank=True, help_text='Digite a bairro aqui.', max_length=100, null=True, verbose_name='Bairro ')),
                ('estado', models.CharField(blank=True, help_text='Digite a estado aqui.', max_length=100, null=True, verbose_name='Estado')),
                ('cep', models.CharField(blank=True, help_text='Digite o cep aqui.', max_length=14, null=True, verbose_name='cep')),
                ('rg', models.CharField(max_length=20, verbose_name='RG')),
                ('cpf', models.CharField(help_text='Digite o CPF aqui modelo: 000.000.000-00', max_length=14, unique=True, verbose_name='CPF')),
                ('num_passaporte', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Número de passaporte')),
                ('finished_at', models.DateField(null=True, verbose_name='Data finalizado')),
                ('anexo1', models.FileField(blank=True, help_text='Envie um arquivo relacionado ao cliente.', null=True, upload_to='anexos/', verbose_name='Anexo')),
                ('anexo2', models.FileField(blank=True, help_text='Envie um arquivo relacionado ao cliente.', null=True, upload_to='anexos/', verbose_name='Anexo')),
                ('anexo3', models.FileField(blank=True, help_text='Envie um arquivo relacionado ao cliente.', null=True, upload_to='anexos/', verbose_name='Anexo')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser_Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('situacao_atual', models.CharField(choices=[('Adm.', 'Administração '), ('Func.', 'Funcionário'), ('Exec', 'Executivo')], default='Adm.', max_length=15, null=True, verbose_name='Situacao atual cargo')),
                ('situacao_atual_empresa', models.CharField(choices=[('Ativo', 'Ativo '), ('Inativo', 'Inativo')], default='Ativo', max_length=15, null=True, verbose_name='Situação atual na empresa')),
                ('salario', models.FloatField(default=0)),
                ('comissao_acumulada', models.FloatField(default=0)),
                ('telefone', models.CharField(blank=True, max_length=15)),
                ('cargo_atual', models.CharField(blank=True, choices=[('Financeiro', 'Financeiro'), ('Despachante', 'Despachante '), ('Despachante externo', 'Despachante externo '), ('Suporte Whatsapp', 'Suporte Whatsapp'), ('Executivo contas', 'Executivo contas')], default='', help_text='A função do empregado é:', max_length=100, null=True, verbose_name='Cargo atual')),
                ('cidade', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('data_nascimento', models.DateField(help_text='Data de nascimento', null=True, verbose_name='Data de nascimento')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='customuser_set', related_query_name='customuser', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_set', related_query_name='customuser', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacaoMensal', models.CharField(blank=True, choices=[('Mensal', 'Mensal'), ('Finalizada', 'Finalizada')], default='Mensal', max_length=10, null=True)),
                ('situacaoMensal_dataApoio', models.DateTimeField(auto_now_add=True)),
                ('data_venda', models.DateField(auto_now_add=True)),
                ('valor', models.FloatField()),
                ('finished_at', models.DateField(null=True, verbose_name='Data finalizado')),
                ('tipo_servico', models.CharField(help_text='Digite o tipo de serviço aqui.', max_length=5000, null=True, verbose_name='Tipo de venda')),
                ('nacionalidade', models.CharField(choices=[('Americano', 'Americano'), ('Canadense', 'Canadense'), ('Mexicano', 'Mexicano'), ('Outros', 'Outros')], default='Americano', max_length=20)),
                ('nacionalidade_outros', models.CharField(blank=True, help_text='Especifique se você escolheu "Outros".', max_length=100, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeAdmin.cadcliente')),
                ('vendedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
