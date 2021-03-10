from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
posts = [
    {
        "author": "akanksha",
        "title": "post 1",
        "content": "first blog post",
        "date": "7th march",
    },
    {
        "author": "jyoti",
        "title": "post 2",
        "content": "second blog post",
        "date": "7th march",
    },
]


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/index.html", context)


def about(request):
    return render(request, "blog/about.html")
