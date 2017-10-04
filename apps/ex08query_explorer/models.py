from django.db import models


class Query(models.Model):
    title = models.CharField('标题', max_length=160)
    description = models.TextField('描述', null=True, blank=True)
    query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
