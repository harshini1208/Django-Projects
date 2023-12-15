from django.contrib import admin
from.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['name','author','published_year','price']
admin.site.register(Book,BookAdmin)
