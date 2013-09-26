"""

link_utils.admin.py
===================

Default admin classes for the django-link-utils
"""
from django.contrib import admin
from django.utils.html import format_html


class LinkTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'show_icon', ]
    fieldsets = (
        (None, {
            'fields': ('name', 'icon'),
        }),
        ('Options', {
            'fields': ('css_classes',),
            'classes': ('collapse',),
        }),
    )

    def show_icon(self, obj):
        return format_html('<img src="%s" />' % (obj.icon.url))


class LinkAdmin(admin.ModelAdmin):
    list_display = ['link_type', 'name', 'url', 'title', ]
    fieldsets = (
        (None, {
            'fields': ('link_type', 'name', 'url'),
        }),
        ('Options', {
            'fields': ('title', 'css_classes', 'target_blank'),
            'classes': ('collapse',),
        }),
    )
