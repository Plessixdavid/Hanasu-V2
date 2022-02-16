# Generated by Django 4.0.1 on 2022-02-15 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0016_delete_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_score', models.IntegerField(blank=True, null=True)),
                ('total_questions', models.IntegerField(blank=True, null=True)),
                ('scores_max', models.IntegerField(blank=True, null=True)),
                ('maneki', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.maneki')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]