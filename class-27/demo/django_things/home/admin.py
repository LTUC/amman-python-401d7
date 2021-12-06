from django.contrib import admin
from .models import Thing
# Register your models here.

#we will be back at 11.16
# @admin.register(Thing)
# class AdminThing(admin.ModelAdmin):
#     list_display= ['name', 'reviewer']
    # search_fields = ['name']
    # list_display_links = ('reviewer',)


admin.site.register(Thing)

