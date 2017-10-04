from django.contrib import admin

from . import models

@admin.register(models.Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('query', 'sql')
    readonly_fields = ('sql',)
