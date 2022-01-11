from django.contrib import admin
from .models import Element

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ['order', 'content']
    search_fields = ['content']
    ordering = ['order']
