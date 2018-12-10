
from django.conf.urls import url
from frontblog import views

urlpatterns = [
    # 用户看到的首页
    url(r'^e_blog/', views.e_blog, name='e_blog'),
    # 点击文章时看到的内容页
    url(r'^e_content/(\d+)/', views.e_content, name='e_content'),
    # 点击关于我时看到的页面
    url(r'^about/', views.about, name='about')
]