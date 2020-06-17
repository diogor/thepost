# Generated by Django 3.0.7 on 2020-06-17 13:11

import apps.post.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('lerd', models.CharField(max_length=300)),
                ('slug', models.SlugField(unique=True, verbose_name='link')),
                ('imagem_destaque', models.ImageField(upload_to=apps.post.models.upload_directory_path)),
                ('texto', models.TextField()),
                ('destaque', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado')),
                ('autor', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='core.Tag', to='core.TagWithHits', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-created_at'],
                'get_latest_by': '-created_at',
            },
        ),
    ]
