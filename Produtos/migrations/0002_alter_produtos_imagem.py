# Generated by Django 4.2.3 on 2023-07-19 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='imagem',
            field=models.ImageField(upload_to='imagens'),
        ),
    ]
