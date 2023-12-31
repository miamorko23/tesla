from django.db import models
from django.contrib.auth.models import User
import secrets


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description


class UserWithKey(User):
    secret_key = models.CharField(max_length=100, default=secrets.token_hex(16))
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    is_manager = models.BooleanField(default=False)
    is_manager_approved = models.BooleanField(default=False)


class DrowsinessEvent(models.Model):
    STATUS_CHOICES = [
        ('W', 'Warning'),
        ('C', 'Critical'),
        ('B', 'Brake Activation'),
        ('BD', 'Brake Deactivated'),
    ]
    user = models.ForeignKey(UserWithKey, on_delete=models.CASCADE)
    time = models.DateTimeField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='W')