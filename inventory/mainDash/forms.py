from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions



from .models import Device, Record

class DeviceRegistrationForm(forms.Form):

    make = forms.CharField(label=' Make', max_length=100)
    model = forms.CharField(label=' Model', max_length=100)
    serial_number = forms.CharField(label=' Serial Number', max_length=100)
    qty = forms.IntegerField(label='Quantity')
    price = forms.IntegerField(label='Price $')
    sellers_origin = forms.CharField(label=' Serial Number', max_length=100)



class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = "__all__"

        
