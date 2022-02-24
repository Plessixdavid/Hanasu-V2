# Generated by Django 4.0.1 on 2022-02-23 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0002_trophy_user_trophy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='maneki',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.maneki'),
        ),
        migrations.AlterField(
            model_name='trophy',
            name='user_trophy',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
