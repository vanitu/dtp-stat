# Generated by Django 2.0 on 2018-04-14 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dtpmapapp', '0008_mvc_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='manufacture_year',
        ),
    ]
