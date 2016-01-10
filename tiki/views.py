from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.template import RequestContext
from time import strftime
from tiki.models import Article


def index(request):
    current_time = strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse('Hello World! <br/> Now=' + str(current_time))


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
