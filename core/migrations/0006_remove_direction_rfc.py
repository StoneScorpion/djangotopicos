# Generated by Django 3.2.7 on 2021-09-28 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_person_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direction',
            name='rfc',
        ),
    ]