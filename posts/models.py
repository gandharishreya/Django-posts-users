from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=65)
    body=models.TextField()
    slug=models.SlugField(unique=True, blank=False, null=False)
    date=models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='Capture3.png', blank= True)

    def __str__(self):
        return self.title
    
