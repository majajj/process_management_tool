from django.db import models
from django.utils.timezone import now


class Process(models.Model):

    pid = models.IntegerField(unique=True)
    status = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    name = models.CharField(max_length=255)
    memory_usage = models.FloatField(help_text="Memory usage in MB or GB")
    cpu_usage = models.FloatField(help_text="CPU usage in percentage")

    @property
    def duration(self):
        return now() - self.start_time

    def __str__(self):
        return f"{self.name} (PID: {self.pid}) - {self.status}"
