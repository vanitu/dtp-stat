# Generated by Django 2.0.4 on 2018-05-02 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dtpmapapp', '0013_auto_20180502_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='street',
            name='region',
        ),
    ]
