from django import forms

from . import models

class LexiqueForm(forms.ModelForm):
    class Meta:
        model = models.Lexique
        fields = ['image', 'romanji', 'traduction', 'description']