from django import forms
from .models import icecream


class icecreamForm(forms.ModelForm):
    class Meta:
        model = icecream
        fields=['name','details','flavours','image']
