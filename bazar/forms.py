from django.forms import ModelForm
from .models import Bazar

class BazarForm(ModelForm):
    class Meta:
        model = Bazar
        fields = ['items', 'amount', 'estimated_cost']