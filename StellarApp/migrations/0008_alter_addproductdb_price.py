# Generated by Django 4.1.2 on 2022-11-26 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StellarApp', '0007_addproductdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproductdb',
            name='Price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
