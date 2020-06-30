# Generated by Django 2.2.13 on 2020-06-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=70, verbose_name='Название')),
                ('price', models.CharField(blank=True, max_length=25, verbose_name='Цена')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Артикул')),
                ('body', models.TextField(blank=True, max_length=150, verbose_name='Аннотация')),
                ('drop_body', models.TextField(blank=True, max_length=350, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары на главной станице',
            },
        ),
    ]
