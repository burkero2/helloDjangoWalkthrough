from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    # Meta provides information about what to render
    class Meta:
        model = Item
        fields = ['name', 'done']
