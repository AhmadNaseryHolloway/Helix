from django import forms
from django.forms import fields
from .models import PurchaseOrder, POLineItems


class PurchaseOrderCreate(forms.ModelForm):
    order_Date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    delivery_Required_Date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data

        return data

class POLineItemCreate(forms.ModelForm):
    class Meta:
        model = POLineItems
        fields = '__all__'