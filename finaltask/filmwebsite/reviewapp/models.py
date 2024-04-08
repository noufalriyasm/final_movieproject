from django.db import models
from filmapp.models import Movie
from django.contrib.auth.models import User

class Rating(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='ratings')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField(choices=[(i,i) for i in range (1,6)])
    created_at=models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)






# Create your models here.
