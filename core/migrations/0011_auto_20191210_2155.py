# Generated by Django 2.2 on 2019-12-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20191210_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.CharField(max_length=50),
        ),
    ]
