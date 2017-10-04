from collections import defaultdict

from django.views.generic import TemplateView

from apps.ex08query_explorer.admin import get_context


class IndexView(TemplateView):
    template_name = 'ex08query_explorer/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # model -> model_name, db_table, full_name, other_full_names
        model_names = defaultdict(list)
        for full_name, model in get_context().items():
            if '.' in full_name:
                _app_label, model_name = full_name.split('.')
                l = model_names[model_name]
                if not l:
                    l.append(model_name)
                    l.append(model._meta.db_table)
                l.append(full_name)
        context['model_names'] = sorted(model_names.values())

        return context
