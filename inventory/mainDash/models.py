from django.db import models

class Device(models.Model):

    device_name = models.CharField(max_length= 50)
    devie_model = models.CharField(max_length= 50)
    device_serial_number = models.CharField(max_length= 50)
    device_qty = models.IntegerField()
    device_price = models.IntegerField()
    device_sellers_origin = models.CharField(max_length= 50)


class Record(models.Model):
    transaction = models.CharField(max_length=50)
    datetime = models.DateField()
    notes = models.CharField(max_length= 50)
    assignee = models.ForeignKey(Device,on_delete=models.PROTECT)
    