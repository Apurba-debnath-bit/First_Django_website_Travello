from django.db import models
#converting class as a Model. 
class Destination(models.Model):
    
    name = models.CharField(max_length=20)
    desc = models.TextField()
    img =  models.ImageField(upload_to="pics")
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


# Create your models here.
