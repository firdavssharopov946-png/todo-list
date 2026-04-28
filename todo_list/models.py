from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)

    STATUS_CHOICES = [
        ('yangi', 'Yangi'),
        ('jarayonda', 'Jarayonda'),
        ('bajarildi', 'Bajarildi'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='yangi')

    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
