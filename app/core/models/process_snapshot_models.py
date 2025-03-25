from django.db import models
from .user_models import User

class ProcessSnapshot(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    processes = models.JSONField()

    def __str__(self):
        return f"Snapshot by {self.author} at {self.timestamp}"