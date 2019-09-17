from rest_framework.views import APIView
from blog import  models
from blog.Error.Error import MyError
from blog.ResponseMsg.ResponMsg import Response_msg
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from blog.ModelsSerializer.ModelsSerizalizer import ArticleSerializer
from blog.module.RestFrameworkModule import MyThrottle
from  blog.module.RewriteModule import Throttled
from django.db.models import Avg, Sum, Max, Min, Count
from django.db import  transaction
# 从session中获取用户id，校验用户是否正确
class vaild_user(object):
    # 获取前端传来的数据
    def __init__(self,request,username,user_id):
        self.username=username
        self.user_id=user_id
        self.request=request

    def valid(self):
        # 判断当前用户是否正确
        user_id = self.request.session.get('_auth_user_id')
        user_obj = models.UserInfo.objects.filter(nid=user_id).first()
        if user_obj.username != self.username:
            raise MyError('300', '(ノ｀Д)ノ滚，冒充用户')
        return user_obj

class article_detail(ViewSetMixin,APIView):

    throttle_classes = [MyThrottle]
    #重写抛出异常
    def throttled(self, request, wait):
        raise  Throttled(wait)
    # 查看文章详情,更改的时候也是这
    def list(self,request,*args,**kwargs):
        ret=Response_msg()
        try:
            # 获取前端传过来的数值
            username=kwargs.get('username')
            article_id=kwargs.get('pk')
            # 从数据库匹配用户还有文章是否正确
            user = models.UserInfo.objects.filter(username=username).first()
            if  user:
                    article = models.Article.objects.filter(user=user, nid=article_id).first()
                    if article:
                        data=ArticleSerializer(article)
                        user_tags=models.Tag.objects.filter(user=user).values('nid','title')
                        blog_category = models.Category.objects.annotate(category_count=Count('article__nid')).values()
                        ret.data={
                            'article_data':data.data,
                            'all_tags':user_tags,
                            'all_category':blog_category
                        }
                    else:
                        raise MyError('404')
            else:
                raise MyError('404')
        except MyError as e:
            ret.code=e.code
        # except Exception as e:
        #     ret.code=200
        #     ret.error='数据库异常'
        return Response(ret.dict)

    # 修改文章内容
    def update(self,request,*args,**kwargs):
        ret=Response_msg()
        try:
            # 验证用户是否正确
            vaild=vaild_user(request,kwargs.get('username'),request.session.get('_auth_user_id'))
            user=vaild.valid()

            article_id=kwargs.get('pk')
            content=request.data.get('content')
            tags_list=request.data.get('tags')  #[1,2]
            category_list=request.data.get('category')
            title=request.data.get('title')
            desc=request.data.get('desc')
            with transaction.atomic():
                article_obj=models.Article.objects.filter(nid=article_id,user=user).first()
                if not article_obj:
                    raise MyError('300','找不到该文章')
                article_detail=models.ArticleDetail.objects.filter(article_id=article_obj.nid).first()
               # 更新数据
                article_detail.content=content
                article_obj.title=title
                article_obj.desc=desc
                article_obj.tags=tags_list
                article_obj.category=category_list
                article_obj.save()
                article_detail.save()
        except MyError as e:
            ret.code=e.code
            ret.error=e.msg
        except Exception as e:
            ret.code='200'
            ret.error='数据库异常'
        return Response(ret.dict)

    # 增加文章
    def create(self,request,*args,**kwargs):
        ret=Response_msg()
        try:
            # 验证用户是否正确
            vaild=vaild_user(request,kwargs.get('username'),request.session.get('_auth_user_id'))
            user=vaild.valid()

            content=request.data.get('content')
            tags_list=request.data.get('tags')  #[1,2]
            category_list=request.data.get('category')
            title=request.data.get('title')
            desc=request.data.get('desc')
            with transaction.atomic():
                
                new_article=models.Article.objects.create(title=title,desc=desc,user=user)
                new_article.tags.add(*tags_list)
                new_article.category.add(*category_list)
                
                models.ArticleDetail.objects.create(content=content,article=new_article)
                
        except MyError as e:
            ret.code=e.code
            ret.error=e.msg
        # except Exception as e:
        #     pass
        return Response(ret.dict)

    # 删除文章
    def destroy(self,request,*args,**kwargs):
        ret=Response_msg()
        try:
            # 验证用户是否正确
            vaild=vaild_user(request,kwargs.get('username'),request.session.get('_auth_user_id'))
            user=vaild.valid()
            # 判断该文章是否存在
            article_id=kwargs.get('pk')
            article_obj=models.Article.objects.filter(user=user,nid=article_id).first()
            if not article_obj:
                raise MyError('300','没有这个文章')
            article_obj.delete()
        except MyError as e:
            ret.code=e.code
            ret.error=e.msg
        # except Exception as e:
        #     pass
        return  Response(ret.dict)


