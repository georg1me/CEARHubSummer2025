from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=25)
    results = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name

class test_event(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
