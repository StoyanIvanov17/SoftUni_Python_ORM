# Generated by Django 5.0.4 on 2024-06-28 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_regularrestaurantreview_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodcriticrestaurantreview',
            options={'ordering': ['-rating'], 'verbose_name': 'Food Critics Review', 'verbose_name_plural': 'Food Critics Reviews'},
        ),
    ]
