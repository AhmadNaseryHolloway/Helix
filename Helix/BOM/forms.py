from django import forms
from .models import BOM, BOMType

class BOMTypeCreateForm(forms.ModelForm):
    class Meta:
        model = BOMType
        fields = '__all__'


class BOMCreateForm(forms.ModelForm):
    class Meta:
        model = BOM
        fields = '__all__'