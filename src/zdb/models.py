from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.URLField()
    release_date = models.DateField()
    duration = models.TimeField()
    director = models.CharField(max_length=50)
    original_lang = models.CharField(max_length=50)
    budget = models.IntegerField()
    income = models.IntegerField()
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title