from django import forms
from .models import PurchaseOrder


class PurchaseOrderCreate(forms.ModelForm):
    order_Date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    delivery_Required_Date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data

        return data