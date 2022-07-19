from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name="Mətn adi")
    explanation = RichTextField(verbose_name="Explanation")
    createdate = models.DateTimeField(verbose_name='createdate',auto_now_add=True)
    author = models.ForeignKey(to="auth.User" ,on_delete= models.CASCADE,verbose_name='Yazıçı')
    