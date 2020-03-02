from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    slug = models.SlugField(null=True, blank=True, default="js2yb8s8ys", unique=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    summary = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title