# Generated by Django 4.1.6 on 2023-02-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devices_id', models.IntegerField()),
                ('device_name', models.CharField(max_length=50)),
                ('devie_model', models.CharField(max_length=50)),
                ('device_serial_number', models.CharField(max_length=50)),
                ('device_qty', models.IntegerField()),
                ('device_price', models.IntegerField()),
                ('device_sellers_origin', models.CharField(max_length=50)),
            ],
        ),
    ]