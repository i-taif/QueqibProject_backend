from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models
#from QueqibApp.models import Profile


class Message(models.Model):
     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')        
     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')        
     message = models.CharField(max_length=1200)
     timestamp = models.DateTimeField(auto_now_add=True)
     def __str__(self):
           return self.message
     class Meta:
           ordering = ('timestamp',)

class Services(models.Model):
    service_name=models.CharField(max_length=80)
    describtion=models.TextField(null=True)
    #profile=models.ForeignKey(Profile,on_delete=CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
         return self.service_name

class Rating(models.Model):
    service=models.ForeignKey(Services,on_delete=models.CASCADE)
    client_user=models.ForeignKey(User,on_delete=models.CASCADE)
    #TourGuide_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='TourGuide')
    star=models.IntegerField(choices=[[1, "1 Star"], [2, "2 Star"], [3, "3 Star"], [4, "4 Star"], [5, "5 Star"]])
    def __str__(self) -> str:
         return self.service.describtion