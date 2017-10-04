import sqlparse
from django.apps import apps
from django.contrib import admin
from django.utils.html import format_html

from . import models


def get_context():
    '''获取所有 Model

    对于每个 Model，返回的字典里可能有两项：

    * model_name -> Model
    * app_label.model_name -> Model

    从而，对于 model_name 重复的情况，可以使用 app_label.model_name 的形式引用。
    '''
    context = {}

    for app_label, models in apps.all_models.items():
        for _, model in models.items():
            class_name = model._meta.object_name
            context[class_name] = model
            context[f'{app_label}.{class_name}'] = model

    return context


@admin.register(models.Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('title', 'formated_query', 'sql', 'created_at')
    readonly_fields = ('sql',)

    def sql(self, obj):
        context = get_context()
        try:
            queryset = eval(obj.query, context)
            sql = str(queryset.query)
        except Exception as exc:
            return format_html(f'<pre>{exc}</pre>')
        sql = sqlparse.format(sql, reindent=True)
        return format_html(f'<pre>{sql}</pre>')

    def formated_query(self, obj):
        return format_html(f'<pre>{obj.query}</pre>')
