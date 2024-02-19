from django.db import models
from django.contrib.auth import get_user_model

class SomeItem(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    rarity = models.CharField(max_length=64, default='Common')  # Additional field for item rarity
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
