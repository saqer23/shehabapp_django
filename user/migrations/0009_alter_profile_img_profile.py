# Generated by Django 3.2.9 on 2022-02-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_profile_occupation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img_profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile_img/'),
        ),
    ]
