# Query Explorer

受 django-sql-explorer 的启发，目的是为了方便学习 Django 的 Query。

## 特点

* Query -> SQL: 管理界面
* 所有的 Model: IndexView

## 用到的知识

* `format_html(format_string, *args, **kwargs)` 
  * （来自 admin 的文档中关于 list_display 的说明）如果给定的 field 是 Model、ModelAdmin 或者是 callable， Django 会对输出进行 HTML-escape。要 escape 用户输入同时允许自己的 tags 不被 escape，可以使用 format_html()。
  * 旧版本（低于 1.9）中，可以使用方法的 allow_tags 属性指定不对结果进行转义，但现在已经不允许了，应该使用更安全的 `format_html()`, `format_html_join()`, or `mark_safe()`。
* `django.apps.apps.all_models`
