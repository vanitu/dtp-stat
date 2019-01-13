# Generated by Django 2.0.5 on 2018-07-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtpmapapp', '0018_mvc_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='mvcparticipanttype',
            name='label',
            field=models.CharField(blank=True, db_index=True, default=None, help_text='MVC Type label', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='mvcparticipanttype',
            name='value',
            field=models.BooleanField(db_index=True, default=True, help_text='Is MVC Type Value at first', max_length=1000),
        ),
    ]
