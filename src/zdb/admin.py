from django.contrib import admin
from .models import Tag, Movie

admin.site.site_header = 'The Zdb admin panel'
admin.site.site_title = 'Zdb panel'

# Register your models here.
class TagAdmin(admin.ModelAdmin): #Tag admin panel config
    pass

class MovieAdmin(admin.ModelAdmin): #Movie admin panel config
    list_display = ('title','release_date','director')    
    search_fields = ['title']

admin.site.register(Tag, TagAdmin)
admin.site.register(Movie, MovieAdmin)
