from django.contrib import admin
from tiki.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'category')

admin.site.register(Article, ArticleAdmin)

