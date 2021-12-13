from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now = True, auto_now_add=False)
    updated = models.DateTimeField(auto_now = False, auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title