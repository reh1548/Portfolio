from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html', {'blogs': Blog.objects.all()})


def blog_single(request, id):
    blog = Blog.objects.get(pk=id)
    return render(request, 'blog/blog_single.html', {'blog': blog})
