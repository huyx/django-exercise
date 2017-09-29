from django.db import models


class Article(models.Model):
    title = models.CharField('标题', max_length=80)
    content = models.TextField('内容')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'

    def __str__(self):
        return self.title
