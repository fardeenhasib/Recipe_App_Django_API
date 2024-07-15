# recipes/models.py
from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.title
