# Generated by Django 5.0.3 on 2024-03-17 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='products', to='shop.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
