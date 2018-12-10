from django.core.paginator import Paginator
from django.shortcuts import render

from endblog.models import Article


def e_blog(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        # 通过Paginator对得到的数据进行切割分页显示
        paginator = Paginator(articles, 5)
        # 获得当前页的页数信息
        page = paginator.page(page)
        return render(request, 'index.html', {'page': page})


def e_content(request, id):
    if request.method == 'GET':
        articles = Article.objects.filter(pk=id).first()

        return render(request, 'content.html', {'content': articles})


def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')

