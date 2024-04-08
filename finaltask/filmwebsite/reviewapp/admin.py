from django.contrib import admin
from .models import Rating,Review

class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie','user','rating']
admin.site.register(Rating,RatingAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie','user','text']
admin.site.register(Review,ReviewAdmin)
# Register your models here.
