# Generated by Django 2.2 on 2019-12-11 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='category',
            new_name='title',
        ),
    ]
