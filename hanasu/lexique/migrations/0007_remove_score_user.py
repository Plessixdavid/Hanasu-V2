# Generated by Django 4.0.1 on 2022-02-15 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lexique', '0006_delete_trophy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='user',
        ),
    ]
