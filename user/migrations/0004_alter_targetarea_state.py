# Generated by Django 3.2.9 on 2022-02-21 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targetarea',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targetArea', to='user.state'),
        ),
    ]
