from django import template
from tiki.models import Article

register = template.Library()


@register.inclusion_tag('random_articles.html')
def random_articles_for_footer():
    # ref: http://stackoverflow.com/a/3506692/198660
    random_articles = Article.objects.all().order_by('?')[:4]
    return {'random_articles': random_articles}
