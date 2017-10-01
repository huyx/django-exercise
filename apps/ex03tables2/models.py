from django.db import models


class Category(models.Model):
    name = models.CharField('分类名', max_length=60)
    parent = models.ForeignKey('self', verbose_name='上级分类', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=80)
    content = models.TextField('内容', default='')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    def actions(self):
        return 'hello'

    actions.verbose_name = '操作'
