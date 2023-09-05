# Generated by Django 4.2.4 on 2023-09-05 00:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PgPrincipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('path', models.ImageField(upload_to='images/')),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('date_create', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]