# Generated by Django 4.1.3 on 2022-12-01 13:40

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("clientes_coches", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="cliente",
            managers=[
                ("clientes", django.db.models.manager.Manager()),
            ],
        ),
    ]