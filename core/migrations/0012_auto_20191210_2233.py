# Generated by Django 2.2 on 2019-12-10 17:03

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20191210_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notisfication',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
