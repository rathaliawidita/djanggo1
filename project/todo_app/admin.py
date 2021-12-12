# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Todo, TodoAdmin)