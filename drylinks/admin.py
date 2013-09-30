"""

drylinks.admin.py
=================

Default admin classes for the django-drylinks application.
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
    list_display = ['name', 'url', 'title', ]
    fieldsets = (
        (None, {
            'fields': ('name', 'url'),
        }),
        ('Options', {
            'fields': ('title', 'css_classes', 'target_blank'),
            'classes': ('collapse',),
        }),
    )


# TODO: inherit from LinkAdmin
class TypedLinkAdmin(LinkAdmin):
    list_display = ['link_type'] + LinkAdmin.list_display
    fieldsets = (
        (None, {
            'fields': ('link_type', 'name', 'url'),
        }),
        ('Options', {
            'fields': ('title', 'css_classes', 'target_blank'),
            'classes': ('collapse',),
        }),
    )
