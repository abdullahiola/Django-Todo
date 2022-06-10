from django.contrib import admin
from . models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
  list_display=['title','id']
  list_per_page = 10

admin.site.register(Todo,TodoAdmin)
