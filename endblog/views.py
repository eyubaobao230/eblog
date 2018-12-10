from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from endblog.ArtForm import EditArtForm, AddArtForm
from endblog.models import Article, SuperUser

from utils.functions import is_login


# 登录页面
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        user = SuperUser.objects.filter(username=username, password=password).first()
        if not user:
            return render(request, 'login.html')

        request.session['user_id'] = user.id
        res = HttpResponseRedirect('/blog/edit/')
        return res


# 登录成功后返回的页面
def edit(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        # 通过Paginator对得到的数据进行切割分页显示
        paginator = Paginator(articles, 5)
        # 获得当前页的页数信息
        page = paginator.page(page)
        return render(request, 'edit.html', {'page': page})


# 添加文章
def add_article(request):
    if request.method == 'GET':
        return render(request, 'add_article.html')
    if request.method == 'POST':
        # 通过ArticleFrom的对象form验证输入的信息是否符合要求
        form = AddArtForm(request.POST, request.FILES)
        # 验证成功，就去获取输入的值，并且保存到数据库中，而后返回文章列表
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            Article.objects.create(title=title, desc=desc, content=content, icon=icon)
            # 通过reverse返回到由namespace和name拼接的url地址
            return HttpResponseRedirect(reverse('editblog:edit'))
        # 验证失败，将错误信息返回到当前网页，不保存错误的信息，不修改地址，只渲染页面
        else:
            return render(request, 'add_article.html', {'form': form})


# 显示文章
def art_list(request):
    if request.method == 'GET':
        # 分页显示
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        # 通过Paginator对得到的数据进行切割分页显示
        paginator = Paginator(articles, 1)
        # 获得当前页的页数信息
        page = paginator.page(page)
        return render(request, 'art_list.html', {'page': page})


# 删除
def del_art_id(request, id):
    if request.method == 'GET':
        # 在数据库中查询与id匹配的数据，并进行删除
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('editblog:edit'))


# 修改
def edit_art_id(request, id):
    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()
        return render(request, 'add_article.html', {'article': article})

    if request.method == 'POST':
        # EditArtForm用作校验
        form = EditArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            # 表示字段验证成功
            article = Article.objects.filter(pk=id).first()
            article.title = title
            article.desc = desc
            article.content = content
            if icon:
                article.icon = icon
            article.save()
            return HttpResponseRedirect(reverse('editblog:edit'))
        else:
            article = Article.objects.filter(pk=id).first()
            return render(request, 'add_article.html', {'form': form, 'article': article})


