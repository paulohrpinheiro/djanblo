from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Post(models.Model):
    """Where content (blog posts) lives"""

    pub_date = models.DateField(auto_now_add=True)
    path = models.TextField(blank=False, unique=True)
    title = models.CharField(max_length=70, blank=False)
    subject = models.CharField(max_length=170, blank=False)
    content = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def  __str__(self):
        """A post identifier"""
        return self.path
