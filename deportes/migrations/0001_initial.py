# Generated by Django 4.1.3 on 2022-12-01 17:50

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Jugador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("equipo", models.CharField(max_length=60)),
                ("edad", models.IntegerField()),
                ("nacionalidad", models.CharField(max_length=50)),
                ("posicion", models.CharField(max_length=60)),
            ],
            managers=[
                ("jugadores", django.db.models.manager.Manager()),
            ],
        ),
    ]