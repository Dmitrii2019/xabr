# Generated by Django 3.1.5 on 2021-02-05 21:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0019_auto_20210206_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xabruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 7, 21, 48, 47, 888982, tzinfo=utc)),
        ),
    ]
