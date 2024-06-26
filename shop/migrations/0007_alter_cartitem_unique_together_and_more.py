# Generated by Django 5.0.3 on 2024-04-22 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_cartitem_review'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('user', 'product')},
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user', 'product')},
        ),
    ]
