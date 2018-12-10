from django.db import models


# 创建文章模型
class Article(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    content = models.TextField()
    icon = models.ImageField(upload_to='article', null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta():
        db_table = 'article'


# 创建登录用户表
class SuperUser(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=16)
    create_time = models.DateTimeField(auto_now_add=True)
    recreate_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'superuser'


# 创建令牌模型
class TokenUser(models.Model):
    token = models.CharField(max_length=30)
    # token和用户表之间是一对一关系
    user = models.OneToOneField(SuperUser)

    class Meta:
        db_table = 'token_user'

