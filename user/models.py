from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username} profili"

class UserSocial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='socials')
    platform_name = models.CharField(max_length=50)  
    link = models.URLField()

    def __str__(self):
        return f"{self.user.username} - {self.platform_name}"

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
    language = models.CharField(max_length=10, default='uz')
    notifications_enabled = models.BooleanField(default=True)
    theme = models.CharField(max_length=10, default='light')

    def __str__(self):
        return f"{self.user.username} sozlamalari"
