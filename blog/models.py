from django.db import models
from django.utils import timezone


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    on_site = models.DateField(default=timezone.now)

    def __str__(self):
        return "%(name)s %(lastname)s" % (
            {'name':self.name, 'lastname':self.last_name})

class Blog(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


