from turtle import onclick
from django.db import models
from django.urls import reverse

class Post(models.Model):
    picture=models.ImageField(upload_to='uploads/',default='uploads/default.jpg')
    title=models.CharField(max_length=255)
    content=models.TextField()
    pub_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"pid": self.id})
    