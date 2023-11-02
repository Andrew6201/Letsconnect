# Generated by Django 4.2.4 on 2023-11-01 23:37

import datetime
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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('job', models.CharField(max_length=2555)),
                ('description', models.CharField(max_length=2550000)),
                ('phonenumber', models.CharField(max_length=15)),
                ('datecreated', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]