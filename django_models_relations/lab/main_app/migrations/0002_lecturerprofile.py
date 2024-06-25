# Generated by Django 5.0.4 on 2024-06-24 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LecturerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('office_location', models.CharField(blank=True, max_length=100, null=True)),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.lecturer')),
            ],
        ),
    ]
