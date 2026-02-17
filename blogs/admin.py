from django.contrib import admin
from .models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'is_published', 'number_of_views',)
    list_filter = ('is_published',)
    search_fields = ('title', 'content',)
