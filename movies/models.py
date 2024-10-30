from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=80)
    
class Person(models.Model):
    name = models.CharField(max_length=120) 
    
class Job(models.Model):
    name = models.CharField(max_length=128)
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    relase_date = models.DateField()
    runnning_time = models.IntegerField()
    budget = models.IntegerField(blank = True)
    tmdb_id = models.IntegerField(blank = True)
    revenue = models.IntergerField(blank = True)
    poster_path = models.IntegerField(blank = True)
    genres = models.ManyToManyField(Genre)
    credits = models.ManyToManyField(Person, through='MovieCredit')
    
    
class MovieCredit(models.Model):
person = models.ForeignKey(Person, on_delete=models.Cascade)
movie = models.ForeignKey(Movie, on_delete=models.Cascade)
job = models.ForeignKey(Job, on_delete=models.Cascade)
    