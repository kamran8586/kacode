from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField()
    video = models.CharField(null = True , blank = True , max_length = 255)
    
    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.text

