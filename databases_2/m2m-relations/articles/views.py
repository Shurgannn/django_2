import json
from pprint import pprint

from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Relationship


def articles_list(request):
    template = 'articles/news.html'
    context = {'object_list': Article.objects.all()}
    articles = Article.objects.all()
    for article in articles:
        print(article)
        scopes = Relationship.objects.filter(article=article)
        for scope in scopes:
            print(scope.thematics.topic)
            print(scope.is_main)
        print('fin')


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
