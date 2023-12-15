from django.contrib import admin

# Register your models here.
from.models import Emp
class EmpAdmin(admin.ModelAdmin):
    list_display=['eno','ename','sal','sex','dno']
admin.site.register(Emp,EmpAdmin)
