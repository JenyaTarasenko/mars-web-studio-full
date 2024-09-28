# Generated by Django 5.0.6 on 2024-06-15 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebSait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='web-site/%Y/%m/%d')),
                ('link', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
                'indexes': [models.Index(fields=['id', 'slug'], name='mars_websai_id_8b19b6_idx'), models.Index(fields=['name'], name='mars_websai_name_c67e6a_idx'), models.Index(fields=['-created'], name='mars_websai_created_5285e5_idx')],
            },
        ),
    ]
