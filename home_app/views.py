from django.shortcuts import render,redirect
from blog.models import Article
from django.urls import reverse


def home(request):
    # articles = Article.objects.all()
    articles = Article.objects.all()
    recent_articles =Article.objects.all()
    return render(request,"home_app/index.html",{"articles":articles})

def sidebar(request):
    data = {'name':'amirhossein'}
    return  render(request,'includes/sidebar.html',context=data)
