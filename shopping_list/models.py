from django.db import models

import uuid

# Create your models here.
class ShoppingItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    purchased = models.BooleanField()

    def __str__(self):
        return f"{self.name}"