# Generated by Django 3.1.5 on 2021-02-20 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210220_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_active',
            field=models.CharField(choices=[('True', 'Опубликована'), ('MD', 'На модерации'), ('False', 'Черновик')], max_length=128, verbose_name='статус'),
        ),
    ]
