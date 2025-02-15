from django.db import models

# Create your models here.
class Records(models.Model):
    Date_time = models.DateTimeField()
    open = models.IntegerField()
    high  = models.IntegerField()
    low = models.IntegerField()
    close = models.IntegerField()
    volume = models.IntegerField()
    
    def __str__(self):
        return f"Day:{self.Date_time} Open:{self.open} High:{self.high} Low:{self.low} Close:{self.close} Volume:{self.volume}"