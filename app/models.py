from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    img = models.URLField(max_length=100)
    description = models.TextField()

class PortfolioPost(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default="Default description")
    
