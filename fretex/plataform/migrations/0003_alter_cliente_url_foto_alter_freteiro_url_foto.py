# Generated by Django 4.0.6 on 2022-08-13 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataform', '0002_alter_produto_imagem_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='url_foto',
            field=models.ImageField(blank=True, null=True, upload_to='cliente'),
        ),
        migrations.AlterField(
            model_name='freteiro',
            name='url_foto',
            field=models.ImageField(blank=True, null=True, upload_to='freteiro'),
        ),
    ]
