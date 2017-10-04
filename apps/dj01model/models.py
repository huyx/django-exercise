'''
用于演示 Django Model 的各项功能，尽量简化不必要的字段。模型中保留了如下特性：

* 基本字段： CharField, IntegerField, DateField
* 外键： ForeignKey
* 多对多： ManyToManyField
'''
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog'


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'


class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    pub_date = models.DateField()
    authors = models.ManyToManyField(Author)
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

    class Meta:
        db_table = 'entry'


class Query(models.Model):
    title = models.CharField(max_length=160)
    query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)

    def sql(self):
        context = {
            'Blog': Blog,
            'Author': Author,
            'Entry': Entry,
        }
        try:
            queryset = eval(self.query, context)
        except Exception as exc:
            return str(exc)
        return str(queryset.query)
