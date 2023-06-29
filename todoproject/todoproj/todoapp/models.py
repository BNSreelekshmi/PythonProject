from django.db import models

# Create your models here.
class task(models.Model):
    tname = models.CharField(max_length=250)
    tpriority = models.IntegerField()
    tdate = models.DateField()

    def __str__(self):
        return self.tname


