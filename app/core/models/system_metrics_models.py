from django.db import models

class SystemMetric(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    cpu_usage = models.FloatField(help_text="System-wide CPU usage percentage")
    memory_usage = models.FloatField(help_text="System-wide memory usage in MB or GB")
    running_processes = models.IntegerField(help_text="Number of currently running processes")

    def __str__(self):
        return f"Metrics at {self.timestamp}: CPU {self.cpu_usage}%, Memory {self.memory_usage}MB, Running {self.running_processes} processes"
