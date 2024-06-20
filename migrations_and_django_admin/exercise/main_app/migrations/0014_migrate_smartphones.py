# Generated by Django 5.0.4 on 2024-06-20 11:31

from django.db import migrations


def set_price(apps, schema_editor):
    MULTIPLY_PRICE = 120

    smartphone_model = apps.get_model('main_app', 'Smartphone')
    smartphones = smartphone_model.objects.all()

    for smartphone in smartphones:
        smartphone.price = len(smartphone.brand) * MULTIPLY_PRICE

    smartphone_model.objects.bulk_update(smartphones, ['price'])


def set_category(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')
    smartphones = smartphone_model.objects.all()

    for smartphone in smartphones:
        if smartphone.price >= 750:
            smartphone.category = 'Expensive'
        else:
            smartphone.category = 'Cheap'

    smartphone_model.objects.bulk_update(smartphones, ['category'])


def set_category_and_price(apps, schema_editor):
    set_price(apps, schema_editor)
    set_category(apps, schema_editor)


def reverse_code(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')
    smartphones = smartphone_model.objects.all()

    for smartphone in smartphones:
        smartphone.price = smartphone_model._meta.get_field('price').default
        smartphone.category = smartphone_model._meta.get_field('category').default

    smartphone_model.objects.bulk_update(smartphones, ['price', 'category'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_smartphone'),
    ]

    operations = [
        migrations.RunPython(set_category_and_price, reverse_code=reverse_code),
    ]
