from django import forms
from .models import List, Item


class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name'}),
        }


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('list', 'primary', 'secondary', 'comments',)
        widgets = {
            'list': forms.Select(attrs={'class': 'form-control',
                                           'placeholder': 'List'}),
            'primary': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Primary'}),
            'secondary': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Secondary'}),
            'comments': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Comments'}),
        }
