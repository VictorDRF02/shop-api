# Generated by Django 5.0.3 on 2024-05-08 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_rename_images_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
