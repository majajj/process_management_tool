from django.db import models
from .user_models import User

class ProcessKillLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    process_name = models.CharField(max_length=255)
    pid = models.IntegerField()

    def __str__(self):
        return f"{self.process_name} (PID: {self.pid}) killed by {self.author} at {self.timestamp}"