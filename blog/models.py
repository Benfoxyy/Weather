from turtle import onclick
from django.db import models

class Post(models.Model):
    picture=models.ImageField(upload_to='uploads/',default='uploads/default.jpg')
    title=models.CharField(max_length=255)
    content=models.TextField()
    def __str__(self):
        return self.title