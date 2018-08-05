from django.shortcuts import render, redirect
from .models import User, Blog
from .forms import BlogForm
from django.utils import timezone


# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


def add(request):
    if request.method == 'POST':
        formset = BlogForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/blog/')
    else:
        formset = BlogForm()
    return render(request, 'blog/add.html', {'formset': formset})


def blog(request):
    blogs = Blog.objects.filter(published_date__lte=timezone.now()) \
        .order_by('-published_date')

    return render(request, 'blog/blog.html', {'blogs': blogs})
