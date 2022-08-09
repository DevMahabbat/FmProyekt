from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField
from django.forms import Widget
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name="Mətn adi")
    explanation = RichTextField(verbose_name="Explanation")
    createdate = models.DateTimeField(verbose_name='createdate',auto_now_add=True)
    author = models.ForeignKey(to="auth.User" ,on_delete= models.CASCADE,verbose_name='Yazıçı')
    
class CodeModel(models.Model):
    
    coder = models.ForeignKey(to="auth.User" ,on_delete= models.CASCADE,verbose_name='Yazıçı',null=True)
    code = models.CharField(max_length=3000,verbose_name="code")
    file =models.FileField(blank = True,null = True,verbose_name="Fayl elave edin",upload_to='media')
    
    