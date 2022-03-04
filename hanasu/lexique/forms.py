from django import forms
from .models import Comment
from lexique import models

class LexiqueForm(forms.ModelForm):
    class Meta:
        model = models.Lexique
        fields = ['image', 'romanji', 'traduction', 'description']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')