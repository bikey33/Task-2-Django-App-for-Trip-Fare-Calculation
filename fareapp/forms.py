from django import forms
from .models import Faredata
class DataForm(forms.ModelForm):
    class Meta:
        model = Faredata
        fields = ['time', 'initial_fare']