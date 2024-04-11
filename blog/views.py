from django.shortcuts import render
from django.http import HttpResponse
from .models import post


def home(request):
    posts = {"posts": post.objects.all(), "title": "Home"}
    return render(request,'blog/home.html',posts)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
