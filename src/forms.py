from django import forms
from .models import blog
from django.forms.widgets import NumberInput


class AddBlog(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    # date = forms.DateField(label="Date",required=True, widget=NumberInput(attrs={'type':'date' , "class": "form-control"}))
    class Meta:
        model = blog
        exclude = ('user',)



