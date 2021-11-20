from django.shortcuts import render
from django.http import  HttpResponse
from .models import Category, Post
# Create your views here.
def home(request):
     posts=Post.objects.all()

     return  render(request,'api/index.html',{'posts':posts})

def post(request , url):
     post=Post.objects.get(url=url)
     print(post)
     return render(request , 'api/post.html',{'post':post})


def about(request):
     return  render(request,'api/about.html')


def help(request):
     return  render(request,'api/help.html')

def career(request):
     return  render(request,'api/career.html')