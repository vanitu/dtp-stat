# Generated by Django 2.1 on 2019-01-10 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dtpmapapp', '0019_auto_20180718_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.DateField(db_index=True, help_text='Update term')),
                ('last_update', models.DateField(db_index=True, help_text='Update date')),
                ('area', models.ForeignKey(help_text='Region/area', on_delete=django.db.models.deletion.CASCADE, to='dtpmapapp.Region')),
            ],
        ),
    ]
