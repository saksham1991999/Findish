# Generated by Django 2.2 on 2019-12-10 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20191211_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeslideshow',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='homeslideshow',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='randdslideshow',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='randdslideshow',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]