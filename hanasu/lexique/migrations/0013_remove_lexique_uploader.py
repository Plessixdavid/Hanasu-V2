# Generated by Django 4.0.1 on 2022-02-16 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lexique', '0012_blog_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lexique',
            name='uploader',
        ),
    ]
