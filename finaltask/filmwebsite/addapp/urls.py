from .import views
from django.urls import path

app_name='addapp'

urlpatterns=[
    path('',views.add_movie,name="add_movie"),
    path('edit_movie/<int:movie_id>/',views.edit_movie,name="edit_movie"),
    path('delete_movie/<int:movie_id>/',views. delete_movie,name="delete_movie"),



]

