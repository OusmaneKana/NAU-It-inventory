from django.db import models

# Create your models here.
class Devices(models.Model):
    devices_id = models.IntegerField()
    device_name = models.CharField(max_length= 50)
    devie_model = models.CharField(max_length= 50)
    device_serial_number = models.CharField(max_length= 50)
    device_qty = models.IntegerField()
    device_price = models.IntegerField()
    device_sellers_origin = models.CharField(max_length= 50)

