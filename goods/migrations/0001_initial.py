# Generated by Django 4.2.7 on 2024-10-09 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('image', models.ImageField(upload_to='images', verbose_name='Изображение')),
                ('content', models.TextField(max_length=3000, verbose_name='Описание товара')),
                ('price', models.IntegerField(verbose_name='Стоимость товара')),
            ],
        ),
    ]
