from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('filmapp:products_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Movie(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    description=models.TextField(max_length=50,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product',blank=True)
    actors=models.TextField(max_length=300)
    available_to_watch = models.BooleanField(default=True)
    released=models.DateTimeField(auto_now_add=True)
    link=models.URLField()
    added_by=models.ForeignKey(User,on_delete=models.CASCADE)


    def get_url(self):
        return reverse('filmapp:movieCatdetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering=('name',)
        verbose_name='movie'
        verbose_name_plural='movies'

    def __str__(self):
        return '{}'.format(self.name)


