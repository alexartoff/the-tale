# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models

class ActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'leader', 'type', 'state', 'percents', 'created_at', 'hero', 'order')

    list_filter = ('type', 'hero')

admin.site.register(models.Action, ActionAdmin)
