# Generated by Django 2.0 on 2018-04-14 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtpmapapp', '0003_auto_20180414_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='offences',
            field=models.ManyToManyField(db_index=True, help_text='Participant offences', to='dtpmapapp.Offence'),
        ),
    ]
