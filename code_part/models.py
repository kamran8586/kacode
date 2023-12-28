from django.db import models
from register_login.models import UserProfile as User
# Create your models here.
class Problem(models.Model):
    DIFFICULTIES = [
        ('EASY' , 'Easy'),
        ('MEDIUM' , 'Medium'),
        ('HARD' , 'Hard')
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=20 , choices = DIFFICULTIES , default = 'EASY')
    
    def __str__(self) -> str:
        return self.title
    
class Submission(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    problem = models.ForeignKey(Problem , on_delete = models.CASCADE)
    code = models.TextField()
    output = models.TextField(null = True , blank = True)
    input_data = models.TextField(null = True , blank = True)
    
    def __str__(self) -> str:
        return self.user.first_name + " " + self.user.last_name + " " + self.problem.title
    