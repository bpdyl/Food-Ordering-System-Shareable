# Generated by Django 3.1.7 on 2021-05-08 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210507_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
