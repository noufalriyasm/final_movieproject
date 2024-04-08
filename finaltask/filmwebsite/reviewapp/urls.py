from django.urls import path
from . import views

app_name='reviewapp'

urlpatterns=[
    path('rating/<int:movie_id>/',views.add_rating,name='add_rating'),
    path('comment/<int:movie_id>/',views.add_review,name='add_comment'),
]
