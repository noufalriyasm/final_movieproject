from django.urls import path
from . import views

app_name='updateapp'

urlpatterns=[
    path('',views.your_profile,name="your_profile")
]
