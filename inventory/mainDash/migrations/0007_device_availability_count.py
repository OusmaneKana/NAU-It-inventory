# Generated by Django 4.1.6 on 2023-03-28 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainDash', '0006_record_assigne_name_record_assigne_room_num_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='availability_count',
            field=models.IntegerField(default=0),
        ),
    ]