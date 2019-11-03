from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Post


def index(request):
    return redirect('panel:news')


def news(request):
    posts = Post.objects.all()    
    return render(request, 'panel/news.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, 
                                                    pub_date__day=day, slug=post)
    return render(request, 'panel/post_detail.html', {'post': post})