# Generated by Django 3.1 on 2021-02-16 19:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210216_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xabruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 18, 19, 54, 33, 38413, tzinfo=utc)),
        ),
    ]
