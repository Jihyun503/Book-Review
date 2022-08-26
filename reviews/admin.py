from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Board)
class BoardAdmin(SummernoteModelAdmin):
    summernote_fields = ('contents',)
    list_display = (
        'bno',
        'title',
        'contents',
        'writer',
        'category',
        'write_date',
        'update_date',
        'hits',
        'meta_json'
    )
    list_display_links = list_display