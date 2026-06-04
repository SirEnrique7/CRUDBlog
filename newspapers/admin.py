from django.contrib import admin
from .models import blog

# Register your models here.
class blogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author__username')
admin.site.register(blog, blogAdmin)

