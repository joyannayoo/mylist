from django.db import models
from boards.models import Board

# Create your models here.
class Item(models.Model):
    item = models.CharField(max_length=100)
    board = models.ForeignKey(to=Board, related_name='items', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.item}'
