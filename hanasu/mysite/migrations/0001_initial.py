# Generated by Django 4.0.1 on 2022-02-18 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Ideogramm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('romanji', models.CharField(max_length=50, null=True)),
                ('Img_link', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ideotype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Maneki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.documentary')),
                ('ideogramm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.ideogramm')),
            ],
        ),
        migrations.CreateModel(
            name='Trophy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trophy_name', models.CharField(blank=True, max_length=255, null=True)),
                ('trophy_score', models.IntegerField(blank=True, default=0, null=True)),
                ('link', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_score', models.IntegerField(blank=True, default=0, null=True)),
                ('total_questions', models.IntegerField(blank=True, default=0, null=True)),
                ('scores_max', models.IntegerField(blank=True, default=0, null=True)),
                ('maneki', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.maneki')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ideogramm',
            name='ideotype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.ideotype'),
        ),
    ]
