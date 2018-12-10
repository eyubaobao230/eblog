from django.conf.urls import url
from endblog import views

urlpatterns = [
    # 注册
    # url(r'^register/', views.register, name='register'),
    # 点击后台管理时看到的登录页面
    url(r'^login/', views.login, name='login'),
    # 登录成功后显示的页面
    url(r'^edit/', views.edit, name='edit'),
    # 点击添加时看到的添加文章页面
    url(r'^add_article/', views.add_article, name='add_article'),
    # 显示文章列表的页面
    url(r'^art_list/', views.art_list, name='art_list'),
    # 删除文章
    url(r'del_art/(\d+)/', views.del_art_id, name='del_art'),
    # 修改文章
    url(r'^edit_art/(\d+)', views.edit_art_id, name='edit_art'),

]


