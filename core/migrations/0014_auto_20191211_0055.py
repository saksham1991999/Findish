# Generated by Django 2.2 on 2019-12-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_homeslideshow_randdslideshow'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeslideshow',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='randdslideshow',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homeslideshow',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='randdslideshow',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
