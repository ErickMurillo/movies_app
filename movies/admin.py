from django.contrib import admin
from .models import *
from django.db.models import Avg

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','rating']

    def rating(self, obj):
        result = Movie.objects.filter(id=obj.id).aggregate(avg = Avg("review__rating"))['avg']
        return result

admin.site.register(Movie,MovieAdmin)
admin.site.register(Review)
