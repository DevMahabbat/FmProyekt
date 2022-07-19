from django.contrib import admin
from django.forms import modelformset_factory

# Register your models here.
from .models import Article
@admin.register(Article)
class App1(admin.ModelAdmin):
    class Meta():
        model = Article
    list_display = ["title","author"]
    search_fields = ['title','author','description']