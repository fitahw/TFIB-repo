from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from .utils import user_avatar_path, user_media_path

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to=user_media_path, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    show_email_publicly = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to=user_avatar_path, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
# Create your models here.
