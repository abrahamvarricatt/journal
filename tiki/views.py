from django.http import Http404
from django.shortcuts import render
from tiki.models import Article


def index(request):
    # Get list of recent articles
    article_list = Article.objects.order_by('-pub_date')[:4]
    if not article_list:
        # No article in DB, show error message
        context = {}
        return render(request,
                      'no_article.html',
                      context)
    else:
        # Show article list page
        context = {
            'articles': article_list
        }
        return render(request,
                      'article_list.html',
                      context)


def article(request, article_id):
    try:
        article_model = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404('Article does not exist')

    # Article context
    context = {
        'title': article_model.title,
        'author': article_model.author,
        'pub_date': article_model.pub_date,
        'category': article_model.category,
        'hero_image': article_model.hero_image,
        'extra_image': article_model.extra_image,
        'body_text': article_model.body_text,
    }
    return render(request,
                  'article.html',
                  context)
