# Generated by Django 4.2.17 on 2024-12-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_dish_photo_url_dish_photo_alter_dish_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='restaurant_photos/'),
        ),
    ]
