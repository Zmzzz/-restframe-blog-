from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

import uuid
import os


# Create your models here.

def user_directory_path(instance, filename):
   ext = filename.split('.')[-1]
     # return the whole path to the file
   return "{0}/{1}/{2}".format(instance.user.username, "avatar", filename)




class Token(models.Model):
    nid=models.AutoField(primary_key=True)
    token=models.CharField(max_length=12)
    user=models.ForeignKey(to='UserInfo')

class UserInfo(AbstractUser):
    """
    用户信息表
    """
    nid = models.AutoField(primary_key=True)
    
    create_time = models.DateTimeField(auto_now_add=True)
    permissions = models.IntegerField(choices=((1,'普通用户'),(2,'vip'),(3,'vvip')),default=1)
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

class UserDetail(models.Model):
    nid=models.AutoField(primary_key=True)
    user=models.OneToOneField(to=UserInfo)
    phone = models.CharField(max_length=11, null=True, unique=True)
    # 上传文件
    avatars = models.ImageField(upload_to=user_directory_path, default="avatars_default/default.jpg", verbose_name="头像")
    avatars_choice=(
        (0, '默认头像'), 
        (1, '用户上传头像'),
    )
    user_avatars= models.IntegerField(choices=avatars_choice, default=0)


class Category(models.Model):
    """博客文章分类
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)  # 分类标题
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name
class Tag(models.Model):
    """
    标签
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32,unique=True)  # 标签名
    user=models.ForeignKey(to='UserInfo',to_field='nid',null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name
class Article(models.Model):
    """
    文章在外面看的数据
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name="文章标题")  # 文章标题
    desc = models.CharField(max_length=255)  # 文章描述
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间

    # 评论数
    comment_count = models.IntegerField(verbose_name="评论数", default=0)
    # 点赞数
    up_count = models.IntegerField(verbose_name="点赞数", default=0)
    # 踩
    down_count = models.IntegerField(verbose_name="踩数", default=0)
    #博客分类
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(to="UserInfo", to_field="nid")
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
class ArticleDetail(models.Model):
    """
    文章详情表 点进去之后看的数据
    """
    nid = models.AutoField(primary_key=True)
    content = models.TextField()
    article = models.ForeignKey(to="Article", to_field="nid")

    class Meta:
        verbose_name = "文章详情"
        verbose_name_plural = verbose_name
class ArticleUpDown(models.Model):
    """
    点赞表
    """
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to="UserInfo", null=True)
    article = models.ForeignKey(to="Article", null=True)
    is_up = models.BooleanField(default=True)

    class Meta:
        unique_together = (("article", "user"),)
        verbose_name = "文章点赞"
        verbose_name_plural = verbose_name
class Comment(models.Model):
    """
    评论表
    """
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="Article", to_field="nid")
    user = models.ForeignKey(to="UserInfo", to_field="nid")
    content = models.CharField(max_length=255)  # 评论内容
    create_time = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey("self", null=True, blank=True)  # blank=True 在django admin里面可以不填
    comment_status=(
        (0, '未被删除'),( 1, '被删除')
    )
    is_delete=models.IntegerField(choices=comment_status,default=0)
    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
