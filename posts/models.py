from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=65)
    body=models.TextField()
    slug=models.SlugField(unique=True, blank=False, null=False)
    date=models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='pic1.jpg', blank= True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
    
