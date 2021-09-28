# Generated by Django 3.2.7 on 2021-09-28 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('birthday', models.DateTimeField()),
                ('age', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Edad')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Peso')),
                ('height', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Altura')),
                ('phone', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('cur', models.CharField(max_length=18, verbose_name='CURP')),
                ('rfc', models.CharField(max_length=12, verbose_name='RFC')),
                ('sex', models.CharField(max_length=1, verbose_name='Sexo')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]