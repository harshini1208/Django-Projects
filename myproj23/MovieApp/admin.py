from django.contrib import admin
from.models  import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['movieid','name','release_date','Director']
admin.site.register(Movie,MovieAdmin)