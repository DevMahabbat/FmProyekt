

from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth import login,authenticate,logout
# Create your views here.

app_name = 'user'
from django.contrib import messages
from .forms import LoginForm, RegisterForm
def register(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.success(request,"Qeydiyyat Ugurla tamamlandir")
            return redirect('index')
            
        context = {
            'form': form
        }
        return render(request,"register.html",context)

    else:
        form  = RegisterForm()
        context = {
            'form': form
        }
    """form = RegisterForm
    context = {
        'form' : form
    }"""

    return render(request,"register.html",context)


def loginF(request):
    form = LoginForm(request.POST or None)
    context ={ 
        "form" :form 
    }

    if form.is_valid():
        username= form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        
        if user is None:
            messages.info(request,"Istifadeci adi ve ya parol yalnisdir")
            return (render,"login.html",context)

        messages.success(request,"Ugurla giris etdiniz")
        login(request,user) 
        return redirect("index") 

    return render(request,"login.html",context)
def logOut(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")