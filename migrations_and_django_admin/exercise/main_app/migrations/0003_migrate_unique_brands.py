# Generated by Django 5.0.4 on 2024-06-19 15:21

from django.db import migrations


def create_unique_brands(apps, schema_editor):
    shoe = apps.get_model('main_app', 'Shoe')
    unique_brands = apps.get_model('main_app', 'UniqueBrands')

    db_alias = schema_editor.connection.alias

    unique_brand_names = shoe.objects.values_list('brand', flat=True).distinct()

    unique_brands_to_create = [unique_brands(brand_name=brand_name) for brand_name in unique_brand_names]

    unique_brands.objects.bulk_create(unique_brands_to_create)

    # for brand_name in unique_brand_names:
    #     unique_brands.objects_using(db_alias).create(brand_name=brand_name)


def delete_unique_brands(apps, schema_editor):
    unique_brands = apps.get_model('main_app', 'UniqueBrands')

    unique_brands.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_uniquebrands'),
    ]

    operations = [
        migrations.RunPython(create_unique_brands, reverse_code=delete_unique_brands)
    ]
