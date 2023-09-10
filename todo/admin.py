from django.contrib import admin
from .models import *


@admin.register(Todo)
class Todo(admin.ModelAdmin):
    list_display = ['title', 'priority', 'is_done']
