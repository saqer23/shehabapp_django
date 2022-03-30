# Generated by Django 3.2.9 on 2022-03-30 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_remove_bill_order'),
        ('chats', '0002_alter_room_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
    ]
