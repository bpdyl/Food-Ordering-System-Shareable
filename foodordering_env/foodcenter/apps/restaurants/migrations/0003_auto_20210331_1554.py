# Generated by Django 3.1.7 on 2021-03-31 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20210331_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restmenumodel',
            name='menu_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
