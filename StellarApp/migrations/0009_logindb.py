# Generated by Django 4.1.2 on 2022-11-28 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StellarApp', '0008_alter_addproductdb_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='logindb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=100, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
