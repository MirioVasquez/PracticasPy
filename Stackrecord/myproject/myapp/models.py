from django.db import models

# Create your models here.
class Records(models.Model):
    Date_time = models.DateTimeField()
    open = models.DecimalField(max_digits=10, decimal_places=4)
    high  = models.DecimalField(max_digits=10, decimal_places=4)
    low = models.DecimalField(max_digits=10, decimal_places=4)
    close = models.DecimalField(max_digits=10, decimal_places=4)
    volume = models.IntegerField()
    
    def __str__(self):
        return f"Day:{self.Date_time} Open:{self.open} High:{self.high} Low:{self.low} Close:{self.close} Volume:{self.volume}"
