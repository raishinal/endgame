from django.db import models
from multiselectfield import MultiSelectField
from datetime import datetime

class Games(models.Model):
    Platform_Choices=(
        ('PC','PC'),
        ('PS4','PS4'),
        ('Xbox','Xbox'),
    )
    Genre_Choices=(
        ('Action','Action'),('Adventure','Adventure'),('Anime','Anime'),('Racing','Racing'),('RPG','RPG'),
        ('Simulation','Simulation'),('Sport','Sport'),('Strategy','Strategy'),('Survival','Survival'),('VR','VR'),
        ('Horror','Horror'),('Shooter','Shooter'),('Puzzle','Puzzle'),('OpenWorld','OpenWorld'),('VisualNovel','VisualNovel'),
    )
    title = models.CharField(max_length = 100)
    site_link = models.CharField(max_length = 100)
    publisher = models.CharField(max_length = 50)
    developer = models.CharField(max_length = 50)
    release_date = models.DateTimeField(default=datetime.now, blank =True)
    posted_date =  models.DateTimeField(default=datetime.now, blank =True)
    overview = models.TextField(blank= True)
    platform = MultiSelectField(choices = Platform_Choices)
    genre = MultiSelectField(choices = Genre_Choices)
    min_cpu = models.CharField(max_length = 50)
    min_ram = models.CharField(max_length = 50)
    min_os = models.CharField(max_length = 50)
    min_videocard = models.CharField(max_length = 50)
    min_storage = models.CharField(max_length = 50)
    rec_cpu = models.CharField(max_length = 50)
    rec_ram = models.CharField(max_length = 50)
    rec_os = models.CharField(max_length = 50)
    rec_videocard = models.CharField(max_length = 50)
    rec_storage = models.CharField(max_length = 50)
    photo_main = models.ImageField(upload_to= 'photos/%Y/%m/%d/')
    screenshot1 = models.ImageField(upload_to= 'photos/%Y/%m/%d/',blank=True)
    screenshot2 = models.ImageField(upload_to= 'photos/%Y/%m/%d/',blank=True)
    screenshot3 = models.ImageField(upload_to= 'photos/%Y/%m/%d/',blank=True)
    screenshot4 = models.ImageField(upload_to= 'photos/%Y/%m/%d/',blank=True)
    screenshot5 = models.ImageField(upload_to= 'photos/%Y/%m/%d/',blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "games"





