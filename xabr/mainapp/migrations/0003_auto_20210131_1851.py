# Generated by Django 3.1 on 2021-01-31 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0002_post_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата добавления')),
                ('moderation', models.BooleanField(default=False, verbose_name='модерация')),
                ('email', models.EmailField(max_length=254)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.post', verbose_name='пост')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
