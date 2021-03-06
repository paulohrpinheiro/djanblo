"""Models for blog app."""

from django.db import models
from django.conf import settings


USER = settings.AUTH_USER_MODEL


class Post(models.Model):
    """Where content (blog posts) lives."""
    pub_date = models.DateTimeField(auto_now_add=True)
    path = models.SlugField(max_length=80, blank=False, unique=True)
    title = models.CharField(max_length=70, blank=False)
    subject = models.CharField(max_length=170, blank=False)
    content = models.TextField(blank=False)
    author = models.ForeignKey(USER, on_delete=models.CASCADE)

    def __str__(self):
        """A post identifier."""
        return self.path

    class Meta():
        index_together = [['pub_date']]
