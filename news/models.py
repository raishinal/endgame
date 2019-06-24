from django.db import models
from datetime import datetime
from games.models import Games
from multiselectfield import MultiSelectField

class News(models.Model):
    title= models.CharField(max_length=200)
    description = models.TextField()
    news_date= models.DateTimeField(default= datetime.now , blank=True)
    image = models.ImageField(upload_to = 'photos/%Y/%m/%d')
    is_trending = models.BooleanField(default= False)
    def __str__(self):
        return self.title
            
    class Meta:
        verbose_name_plural = "News"

