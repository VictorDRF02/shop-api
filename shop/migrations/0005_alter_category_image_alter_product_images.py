# Generated by Django 5.0.3 on 2024-03-24 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/categories/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products/'),
        ),
    ]
