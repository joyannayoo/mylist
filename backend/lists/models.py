from django.db import models
from categories.models import Category

# Create your models here.


class List(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        to=Category, related_name='list', on_delete=models.CASCADE, default=None, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.name}'
