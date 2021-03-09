from django import forms
from ecover.models import Announcement




class UpdateAddForm(forms.ModelForm):
    
    class Meta:
        model = Announcement
        fields = ['title','region','district','address','type','status','view','content','image','price']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control h6'}),
            'region':forms.Select(attrs={'class':'form-control'}),
            'district':forms.Select(attrs={'class':'form-control'}),
            'type':forms.Select(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'view':forms.Select(attrs={'class':'form-control'}),            
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'price':forms.Select(attrs={'class':'form-control'}),

        }

    