from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields

from .models import Post


class Postform(ModelForm):
    class Meta:
        model = Post
        fields = ['heading', 'categories', 'tags', 'content']
        
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }