# Generated by Django 3.2.7 on 2021-09-28 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='diet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.diet', verbose_name='Dieta'),
        ),
    ]
