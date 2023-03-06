# from django.db import models
from djongo import models
import uuid
class Device(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_name = models.CharField(max_length= 50)
    devie_model = models.CharField(max_length= 50)
    device_serial_number = models.CharField(max_length= 50)
    device_qty = models.IntegerField()
    device_price = models.IntegerField()
    device_sellers_origin = models.CharField(max_length= 50)


class Record(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction = models.CharField(max_length=50)
    datetime = models.DateField()
    notes = models.CharField(max_length= 50)
    device = models.ForeignKey(Device,on_delete=models.PROTECT)
    