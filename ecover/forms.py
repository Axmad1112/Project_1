from django import forms
from ecover.models import Announcement




class UpdateAddForm(forms.ModelForm):
    
    class Meta:
        model = Announcement
        fields = ['title','region','district','address','type','status','view','content','image','price','phone']
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
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.Select(attrs={'class':'form-control'}),

        }

class SearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Search name or surname!',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )

    search_price_exact = forms.IntegerField(
                    required = False,
                    label='Search price (exact match)!'
                  )

    search_price_min = forms.IntegerField(
                    required = False,
                    label='Min age'
                  )


    search_price_max = forms.IntegerField(
                    required = False,
                    label='Max age'
    )
       