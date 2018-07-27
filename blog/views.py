from django.shortcuts import render
from .models import User, Blog
from django.utils import timezone
# Create your views here.

def index(request):
    blogs = Blog.objects.filter(published_date__lte=timezone.now())\
        .order_by('published_date')

    return render(request, 'blog/index.html', {'blogs':blogs})