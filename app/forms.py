
from django import forms

from app.models import Article
 



class Articleform(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'explanation']
        