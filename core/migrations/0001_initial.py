# Generated by Django 2.2 on 2019-12-08 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='board_of_members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Designation', models.CharField(max_length=50)),
                ('Contact', models.CharField(max_length=50)),
            ],
        ),
    ]