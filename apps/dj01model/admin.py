from django.contrib import admin

from . import models


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('query', 'sql')
    readonly_fields = ('sql',)
