from django.db import models
import datetime
# Create your models here.
class CSVStore(models.Model):
    user_name = models.CharField(max_length=200)
    user_text = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)