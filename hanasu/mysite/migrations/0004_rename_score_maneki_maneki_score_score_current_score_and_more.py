# Generated by Django 4.0.1 on 2022-02-09 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maneki',
            old_name='score',
            new_name='maneki_score',
        ),
        migrations.AddField(
            model_name='score',
            name='current_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='score_maneki',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.maneki'),
        ),
    ]
