from django import forms
from django.forms.widgets import TextInput, ChoiceWidget, HiddenInput, Textarea
from ecover.models import Announcement, Region, District, Status, View, Type
from django.forms.fields import ImageField, CharField, ChoiceField



class AddForm(forms.ModelForm):
    
    class Meta:
        model = Announcement
        fields = ['title','address','type','status','view','content','image','price','phone','person_name']
    # title = forms.CharField(
    #     max_length=50, required=True,
    #     widget=forms.TextInput(attrs={
    #         'name': 'title',
    #         'id': 'title_id',
    #         'placeholder': 'Title',
    #         'required': 'required'
            
    #     })
    # )
    # regions=tuple([tuple(i.name,) for i in Region.objects.all()])
    # region = forms.ChoiceField(
    #     choices=regions,
    #     widget=ChoiceWidget(attrs={
    #         'name': 'region',
    #         'id': 'region_id',
    #         'class':'region'
                       
    #     })
    # )
    
    # region_id = forms.CharField(
    #     widget=HiddenInput(attrs={
    #         'name': 'region_id',
    #         'id': 'region_id',
    #     })
    # )

    # districts = tuple([tuple(i.name,) for i in District.objects.all()])
    # district = forms.ChoiceField(
    #     choices = districts,
    #     widget = ChoiceWidget(attrs={
    #         'name': 'district',
    #         'id': 'district_id'
            
    #     })
    # )

    # address = forms.CharField(
    #     max_length=50,
    #     widget = forms.TextInput(attrs={
    #         'name': 'addres',
    #         'id': 'adress_id',
    #     })
    # )

    # types = tuple([tuple(i.name,) for i in Type.objects.all()])
    # type = forms.ChoiceField(
    #     choices=types,
    #     widget = ChoiceWidget(attrs={
    #         'name': 'type',
    #         'id': 'type_id',
    #     })
    # )
    # statuses = tuple([tuple(i.name,) for i in Status.objects.all()])
    # status = forms.ChoiceField(
    #     choices=statuses,
    #     widget = ChoiceWidget(attrs={
    #         'name': 'status',
    #         'id': 'status_id',
    #     })
    # )

    # views = tuple([tuple(i.name,) for i in View.objects.all()])
    # view = forms.ChoiceField(
    #     choices=views,
    #     widget = ChoiceWidget(attrs={
    #         'name': 'view',
    #         'id': 'view_id',
    #     })
    # )

    # content = forms.CharField(
    #     max_length=80,
    #     widget=forms.Textarea(attrs={
    #         'name': 'content',
    #         'id': 'content',
    #         'placeholder': 'Content',
    #         'required':'required'
    #     })
    # )

    
    # image = forms.ImageField()


    # price = forms.FloatField(
    #     widget= forms.NumberInput(attrs={
    #         'name': 'price'
    #     })
    # )
  

    # person_name = forms.CharField(
    #     max_length=30,
    #     widget = forms.TextInput(attrs={
    #         'name': 'person_name'
    #     })
    # )
    

    # phone = forms.CharField(
    #     max_length=20,
    #     widget=forms.TextInput(attrs={
    #         'name': 'phone',
    #         'id': 'phone_id',
    #         'placeholder': 'Phone number',
    #         'required':'required'
    #     }))

