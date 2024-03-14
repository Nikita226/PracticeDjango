from django.db import models

# Create your models here.
class Data(models.Model):
    nname = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.nname}"

class Subject(models.Model):
    subject = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.subject}"