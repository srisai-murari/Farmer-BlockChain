
from django.db import models

class Block(models.Model):
    index = models.IntegerField()
    timestamp = models.FloatField()
    transactions = models.TextField()
    previous_hash = models.CharField(max_length=256)
    hash = models.CharField(max_length=256)

    def __str__(self):
        return f"Block {self.index}"
