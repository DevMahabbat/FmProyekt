from django.shortcuts import  render,HttpResponse,redirect,get_object_or_404,reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import  Articleform
from .models import Article
from .forms import CodeForm
import os
from pathlib import Path
def index(request):
    return  render(request,"index.html")



def about(request,id):
    context = {'id':id}
    return HttpResponse("about")




@login_required
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
        return redirect('dashboard')

        
    return render(request,"addarticle.html",{"form":form})



@login_required
def detail(request,id):
    article = Article.objects.filter(id=id).first()
    return render(request,"detail.html",{"article":article})



@login_required 
def detailhell(request,id):
    article = Article.objects.filter(id=id).first()
    form = CodeForm(request.POST or None, request.FILES or None)
    
    
    if form.is_valid():
        myfile = form.save(commit= False)
        myfile.coder = request.user
        myfile.file = request.FILES.get('file')
        filename = str(myfile.file)
        myfile.save()
        BASE_DIR = Path(__file__).resolve().parent.parent
        filedir = os.path.join(BASE_DIR, 'media',filename)
        print(filedir)
        print(filename)
        myfile.save()
        # rufet filedir senin ucun pomoy komputerde yuklenen faylin harda oldugun deyir adi da daxil olmaqla, filename ise hemin faylin adidi



        messages.success(request,message ='code saved successfully')
        return redirect('dashboard')

        #  get code and write it to the file 
        print(form)
        with open('form.txt', 'w') as file:
            file.writelines(str(form))
        with open('form.txt','r+',encoding='utf-8') as file1:
            metn = file1.read()
            metn2 = str(metn[178:-59])     
        print(metn2)
        with open('textin2.txt','w',encoding='utf-8') as file2:
            file2.write(metn2)
        

    context = {"article":article,
    "form":form}
    return render(request,"detailhell.html",context=context) 