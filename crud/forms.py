from django import forms
from crud import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['slug', 'title', 'summary', 'description']