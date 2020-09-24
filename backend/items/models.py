from django.db import models
from boards.models import Board

# Create your models here.
class Item(models.Model):
    item = models.CharField(max_length=100)
    board = models.ForeignKey(to=Board, related_name='items', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    notes = models.TextField(max_length=500, blank=True, default=True)
    url = models.URLField(max_length=250, default=None, blank=True, null=True)
    image = models.ImageField(upload_to=None)
    index = models.PositiveIntegerField()
    tags = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}: {self.item}'
