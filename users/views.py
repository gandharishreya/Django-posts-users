
from http.client import HTTPResponse
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.

def register_view(request):
    #posts=Post.objects.all().order_by('-date')
    if request.method =="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            print("form submitted")
            return redirect("posts:list")
        else:
            print("❌ Form errors:", form.errors)
    else:
        form=UserCreationForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")
    else:
        form=AuthenticationForm()

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
        if request.method=="POST":
            logout(request)
            return redirect("posts:list")

    #return render(request, "users/logout.html", {"form": form})

