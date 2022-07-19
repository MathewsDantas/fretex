# Generated by Django 4.0.6 on 2022-07-19 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_foto', models.ImageField(blank=True, null=True, upload_to=None)),
                ('cpf', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=100)),
                ('CEP', models.CharField(max_length=9)),
                ('numero', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('complemento', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Freteiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_foto', models.ImageField(blank=True, null=True, upload_to=None)),
                ('cpf', models.CharField(max_length=15)),
                ('endereco', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='plataform.endereco')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', models.CharField(max_length=300)),
                ('nomeDestinatario', models.CharField(max_length=200)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataform.cliente')),
                ('freteiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataform.freteiro')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('imagem_url', models.ImageField(blank=True, null=True, upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TipoVeiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=20)),
                ('cor', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('ano', models.CharField(max_length=4)),
                ('tipo_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataform.tipoveiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Proposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('ehAceita', models.BooleanField(default=False)),
                ('ehContraproposta', models.BooleanField(default=False)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataform.pedido')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataform.veiculo')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataform.produto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataform.status'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='tipo_veiculo',
            field=models.ManyToManyField(to='plataform.tipoveiculo'),
        ),
    ]
