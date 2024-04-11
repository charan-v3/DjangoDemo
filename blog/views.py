from django.shortcuts import render
from django.http import HttpResponse

post=[
    {
        'title':'Love',
        'author':'Charan',
        'content':'Secret of Love',
        'date_posted':'30 Sep 2004'
    }
    ,    {
        'title':'Friendship',
        'author':'Aku',
        'content':'Secret of Friendship',
        'date_posted':'14 Nov 2004'
    }
]

def home(request):
    posts={
        'posts':post,
        'title':'Home'
    }
    return render(request,'blog/home.html',posts)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})