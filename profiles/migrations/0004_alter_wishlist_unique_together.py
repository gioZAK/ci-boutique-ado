# Generated by Django 3.2 on 2023-01-12 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_wishlist_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wishlist',
            unique_together=set(),
        ),
    ]
