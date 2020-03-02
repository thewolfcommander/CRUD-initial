from django.contrib import admin
from crud import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'updated']
    list_filter = ['user', 'timestamp', 'updated']