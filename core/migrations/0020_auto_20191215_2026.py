# Generated by Django 2.2 on 2019-12-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20191215_0012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='randdslideshow',
            options={'verbose_name_plural': 'Research & Development Slideshow'},
        ),
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
