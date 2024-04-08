from django.contrib import admin
from .models import Category,Movie
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','category','description','released','link']
    list_editable = ['category','description','link']
    prepopulated_fields ={'slug':('name',)}
    list_per_page = 20

admin.site.register(Movie,MovieAdmin)


# class RatingAdmin(admin.ModelAdmin):
#     list_display = ['movie','user','rating','review']
# admin.site.register(ReviewRating,RatingAdmin)

# class RatingAdmin(admin.ModelAdmin):
#     list_display = ['movie','user','rating']
# admin.site.register(Rating, RatingAdmin)
#
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['movie','user','text']
# admin.site.register(Comment,CommentAdmin)