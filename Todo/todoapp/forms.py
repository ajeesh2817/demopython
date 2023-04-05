from django import forms
from .models import todo


class Todoforms(forms.ModelForm):
    class Meta:
        model=todo
        fields=['date','priority']
