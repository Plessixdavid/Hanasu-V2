# Generated by Django 4.0.1 on 2022-02-10 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_rename_score_maneki_score_maneki'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maneki',
            name='maneki_score',
        ),
    ]