
from multiprocessing import context
from tabnanny import verbose
from django import forms

from app.models import Article
 
from django import forms


class Articleform(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'explanation']
        
class CodeForm(forms.Form):
    Code = forms.CharField(max_length=3000,widget=forms.Textarea(attrs={'class': 'form-control'}))
    def clean(self):
        return self.cleaned_data.get("Code")
    
