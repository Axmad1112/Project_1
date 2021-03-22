from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Post_categories)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'post', 'date', 'active')
    list_filter = ('active', 'date')
    search_fields = ('name', 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
# Register your models here.
