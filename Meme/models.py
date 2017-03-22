from django.db import models

# Create your models here.

class img_name(models.Model):
    dte = models.CharField(max_length = 25)
    
    def __str__(self):
        return self.dte + '/1|2|3/.png'
