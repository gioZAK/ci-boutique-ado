# Generated by Django 3.2 on 2023-01-13 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
    ]
