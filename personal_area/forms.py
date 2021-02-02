from django import forms
from django.forms.widgets import TextInput, ChoiceWidget, HiddenInput, Textarea

class AddForm(forms.Form):
    title = forms.CharField(
        max_length=50, required=True,
        widget=forms.TextInput(attrs={
            'name': 'title',
            'id': 'title_id',
            'placeholder': 'Title',
            
        })
    )
    regions=tuple([tuple(i.name,) for i in Region.objects.all()])
    region = forms.ChoiceField(
        choices=regions,
        widget=ChoiceWidget(attrs={
            'name': 'region',
                       
        })
    )
    
    region_id = forms.CharField(
        widget=HiddenInput(attrs={
            'name': 'region_id'
        })
        )


