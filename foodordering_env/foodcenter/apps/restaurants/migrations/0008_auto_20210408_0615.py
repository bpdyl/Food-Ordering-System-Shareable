# Generated by Django 3.1.7 on 2021-04-08 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20210405_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='rest_photo',
            field=models.ImageField(default='user_photos/nouser.jpg', upload_to='user_photos'),
        ),
    ]
