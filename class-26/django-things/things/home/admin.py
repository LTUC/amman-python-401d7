from django.contrib import admin
from .models import Thing
# Register your models here.

@admin.register(Thing)
class AdminThing(admin.ModelAdmin):
    list_display = ['title']