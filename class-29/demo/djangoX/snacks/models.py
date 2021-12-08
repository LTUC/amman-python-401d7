from django.db import models
from django.db.models.base import Model
from django.contrib.auth import get_user_model

class Snack(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
