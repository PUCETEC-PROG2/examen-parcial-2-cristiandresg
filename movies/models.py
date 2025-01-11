from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.IntegerField(primary_key=True )
    title_movie = models.CharField(max_length=30, null=False)
    MOVIE_GENRES = {
        ('A', 'Accion'),
        ('B', 'Biografia'),
        ('C', 'Comedia'),
        ('T', 'Terror')
    }
    
    movie_genre = models.CharField(max_length=30,choices=MOVIE_GENRES, null=False)
    director = models.CharField(max_length=30, null=False)
    release_year = models.DateField()
    sinopsis = models.TextField()
    
    def __str__(self):
        return self.title_movie 
    