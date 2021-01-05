from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    data = models.CharField(max_length=255, verbose_name="Reminders")
    created_date_time = models.DateTimeField(auto_now_add=True)
    dead_line = models.DateTimeField(verbose_name="Deadline")

    def __str__(self):
        return self.title