## 自定义模板标签

### x_var

通过 x_var 可以访问 `_` 开头的变量、属性。

示例：获取 QuerySet 的所有字段：

```djangotemplate
{% load core_tags %}

{% x_var 'article_list.model._meta.fields' as fields %}

{% for field in fields %}
    {{ field.verbose_name }}
{% endfor %}
```
