from typing import Container
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class City(models.Model):
    image=models.URLField(max_length=300)
    City_name=models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    slug=models.SlugField(unique=True)
    def __str__(self) -> str:
        return self.City_name


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image=models.URLField(max_length=300)
    name=models.CharField(max_length=30)
    bio=models.TextField()
    cities=models.ManyToManyField(City)
    slug=models.SlugField(unique=True)
    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title=models.CharField(max_length=50)
    image=models.URLField(max_length=300)
    body=models.CharField(max_length=50)
    start_date=models.DateField(auto_now_add=True)
    cities=models.ForeignKey(City,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    slug=models.SlugField(unique=True)
    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    content=models.TextField()
    comment_date=models.DateField(auto_created=True)
    slug=models.SlugField(unique=True)
    def __str__(self) -> str:
        return self.post,self.content
