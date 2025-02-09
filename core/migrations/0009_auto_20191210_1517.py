# Generated by Django 2.2 on 2019-12-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='city',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='country',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='pincode',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='street_address',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
