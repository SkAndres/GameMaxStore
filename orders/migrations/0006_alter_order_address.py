# Generated by Django 4.0.5 on 2022-07-04 13:08

from django.db import migrations
import places.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_order_geolocation_alter_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=places.fields.PlacesField(max_length=255),
        ),
    ]