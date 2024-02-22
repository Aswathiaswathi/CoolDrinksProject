from django import forms
from .models import drinks


class updrink(forms.ModelForm):
    class Meta:
        model=drinks
        fields='__all__'
        labels={
            "Drinks":"Drink Name",
            "Photo":"Image",
            "Qty":"Litter",
            "Price":"Price",
            "Description":"Description",
        }

            
        

        