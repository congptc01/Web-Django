# Generated by Django 5.0.3 on 2024-04-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('correo', models.CharField(max_length=25)),
                ('telefono', models.IntegerField()),
            ],
            options={
                'db_table': 'tut_usuarios',
            },
        ),
    ]
