from django.db import models
from django.contrib.auth.models import User

class Bazar(models.Model):
    items = models.CharField(max_length=120)
    amount = models.CharField(max_length=120)
    estimated_cost = models.CharField(max_length=22)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.items



