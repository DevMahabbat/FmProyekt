from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from matplotlib.style import context
# Create your views here.
from .forms import  Articleform
from .models import Article


def index(request):
    return  render(request,"index.html")



def about(request,id):
    context = {'id':id}
    return HttpResponse("about")





def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context={'articles': articles}

    return render(request,"dashboard.html",context)



def addArticle(request):
    form = Articleform(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla oluşturuldu")
        return redirect("index")

        
    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    article = Article.objects.filter(id=id).first()
    return render(request,"detail.html",{"article":article})
