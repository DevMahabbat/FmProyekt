
from multiprocessing import context
from tabnanny import verbose
from django import forms

from app.models import Article,CodeModel
 
from django import forms


class Articleform(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'explanation']
        
class CodeForm(forms.ModelForm):
    class Meta:
        model  = CodeModel
        fields = ["code","file"]
