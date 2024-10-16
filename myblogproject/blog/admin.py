from django.contrib import admin
from .models import BlogPost

admin.site.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Show title and creation date in the list view
    search_fields = ('title',)  # Enable searching by title
    list_filter = ('created_at',) 

