# Generated by Django 5.0.4 on 2024-06-17 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_rename_is_favourite_exercise_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='calories_burned',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
