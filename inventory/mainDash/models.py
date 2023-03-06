from django.db import models
import uuid
class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    make = models.CharField(max_length= 50)
    model = models.CharField(max_length= 50)
    serial_number = models.CharField(max_length= 50)
    qty = models.IntegerField()
    price = models.IntegerField()
    sellers_origin = models.CharField(max_length= 50)


class Record(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction = models.CharField(max_length=50)
    datetime = models.DateField()
    notes = models.CharField(max_length= 50)
    device = models.ForeignKey(Device,on_delete=models.PROTECT)
    