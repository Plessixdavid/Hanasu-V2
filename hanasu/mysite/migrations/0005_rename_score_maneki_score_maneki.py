# Generated by Django 4.0.1 on 2022-02-10 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_rename_score_maneki_maneki_score_score_current_score_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='score_maneki',
            new_name='maneki',
        ),
    ]
