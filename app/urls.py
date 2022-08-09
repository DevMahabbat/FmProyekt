


from django import views

from django.urls import path


from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('about/<int:id>',views.about),
    path('dashboard',views.dashboard),
    path('addarticle',views.addArticle),
    path('article/<int:id>',views.detail,name="detail"),
    path('articlehell/<int:id>',views.detailhell,name="detailhell"),
]

