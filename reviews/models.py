from django.db import models
from games.models import Games
from datetime import datetime

class Reviews(models.Model):
    game = models.ForeignKey(Games, on_delete=models.DO_NOTHING)
    title= models.CharField(max_length= 100)
    rating= models.DecimalField(max_digits=2, decimal_places=1)
    price= models.DecimalField(max_digits=2, decimal_places=1)
    graphics= models.DecimalField(max_digits=2, decimal_places=1)
    levels = models.DecimalField(max_digits=2, decimal_places=1)
    difficulty= models.DecimalField(max_digits=2, decimal_places=1)
    detail = models.TextField()


    date= models.DateTimeField(default= datetime.now, blank= True)
    image= models.ImageField(upload_to= 'photos/%Y/%m/%d/')
    is_trending = models.BooleanField(default= False)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Reviews"

     