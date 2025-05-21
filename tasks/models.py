from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(blank=True, null=True)
    priority_choices = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    priority = models.CharField(max_length=1, choices=priority_choices, default='M')

    def __str__(self):
        return self.title
