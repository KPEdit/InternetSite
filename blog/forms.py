from django.forms import models
from .models import Blog, User


class BlogForm(models.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
