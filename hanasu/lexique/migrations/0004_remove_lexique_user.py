# Generated by Django 4.0.1 on 2022-02-23 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lexique', '0003_lexique_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lexique',
            name='user',
        ),
    ]