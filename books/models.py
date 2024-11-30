from django.db import models
import uuid

# Create your models here.

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255) # can't be null NOT NULL is automatically added
    description = models.TextField()
    author = models.CharField(max_length=200, blank=True)
    language = models.CharField(max_length=20, blank=True)
    pages = models.IntegerField(blank=True,  null=True)
    publisher = models.CharField(max_length=50, blank= True)
    published_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add only updates on creation
    
    
    
