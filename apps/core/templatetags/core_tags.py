from django import template

register = template.Library()


class X_Variable(template.Variable):
    def __init__(self, var):
        try:
            super().__init__(var)
        except template.TemplateSyntaxError as exc:
            assert 'not begin with underscores' in exc.args[0]
            from django.template.base import VARIABLE_ATTRIBUTE_SEPARATOR
            self.literal = None
            self.lookups = tuple(var.split(VARIABLE_ATTRIBUTE_SEPARATOR))


@register.simple_tag(takes_context=True)
def x_var(context, var):
    return X_Variable(var).resolve(context)
