# Generated by Django 4.0.5 on 2022-06-26 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imagine',
            new_name='image',
        ),
    ]