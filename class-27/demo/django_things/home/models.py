from django.db import models
from django.contrib.auth import get_user_model


# ORM ----> Object Relational Mapper
class Thing(models.Model):
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)


    def __str__(self):
        return self.name
