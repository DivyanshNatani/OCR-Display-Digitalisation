from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class reading(models.Model):
    time_of_recording = models.DateTimeField()
    reading_value=models.FloatField(blank=False)
    reading_details = models.CharField(max_length=200, default="", blank=True)
    # pub_date = models.DateTimeField("date published")
    

class table_reading(models.Model):
    time_of_recording = models.DateTimeField()
    reading_value=models.FloatField(blank=False)
    reading_details = models.CharField(max_length=200, default="", blank=True)
    # pub_date = models.DateTimeField("date published")
 