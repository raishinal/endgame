from django.db import models
from games.models import Games
from datetime import datetime

class Reviews(models.Model):
    game = models.ForeignKey(Games, on_delete=models.DO_NOTHING)
    title= models.CharField(max_length= 100)
    detail = models.TextField()
    ratings= models.DecimalField(max_digits=2, decimal_places=1)
    date= models.DateTimeField(default= datetime.now, blank= True)
    image= models.ImageField(upload_to= 'photos/%Y/%m/%d/')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Reviews"

     