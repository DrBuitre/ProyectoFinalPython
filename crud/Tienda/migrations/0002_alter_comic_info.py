# Generated by Django 4.1.7 on 2023-04-14 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='info',
            field=models.TextField(max_length=1200),
        ),
    ]