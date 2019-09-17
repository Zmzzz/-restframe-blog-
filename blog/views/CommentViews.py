from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from blog import models
from blog.Error.Error import MyError
from blog.ResponseMsg.ResponMsg import Response_msg
from django.db import transaction
from django.db.models import F



class vaild_user(object):
    # 获取前端传来的数据
    def __init__(self, request, username, user_id):
        self.username = username
        self.user_id = user_id
        self.request = request

    def valid(self):
        # 判断当前用户是否正确
        user_id = self.request.session.get('_auth_user_id')
        user_obj = models.UserInfo.objects.filter(nid=user_id).first()
        if user_obj.username != self.username:
            raise MyError('300', '用户不存在')
        return user_obj
class comment(ViewSetMixin,APIView):

    # 删除评论，其实并没有删除，只是将评论的状态改为1
    def destroy(self,request,*args,**kwargs):
        ret=Response_msg()
        try:
            # 验证用户是否正确
            vaild = vaild_user(request, kwargs.get('username'), request.session.get('_auth_user_id'))
            user = vaild.valid()
            # 判断这个评论是否存在，获取文章id,评论id
            article_id=kwargs.get('article_pk')
            comment_id=kwargs.get('comment_pk')
            comment_obj=models.Comment.objects.filter(article_id=article_id,nid=comment_id).first()
            print(comment_obj,'sasas')
            if not comment_obj:
                raise MyError('300','gun1，不存在')
            comment_obj.is_delete=1
            comment_obj.save()
        except MyError as e:
            ret.code=e.code
            ret.error=e.msg
        return Response(ret.dict)

    # 增加评论
    def create(self,request,*args,**kwargs):
        ret=Response_msg()
        try:
            user_id=request.data.get('user_id')
            # 当前用户的id,评论者
            article_id=request.data.get('article_id')
            content=request.data.get('content')
            parent_id=request.data.get('parent_id')
            print(user_id,article_id,content,parent_id)
            user=models.UserInfo.objects.filter(nid=user_id).first()
            if not user:
                raise MyError('300','没有这个人')
            with transaction.atomic():
                # 创建评论
                if not parent_id:
                    models.Comment.objects.create(user=user,content=content,article_id=article_id)
                else:
                    models.Comment.objects.create(user=user, content=content, article_id=article_id,parent_comment_id=parent_id)
                # 评论数+1
                models.Article.objects.filter(nid=article_id).update(comment_count=F('comment_count')+1)
        except MyError as e:
            ret.code=e.code
            ret.error=e.msg
        # except Exception as  e:
        #     pass
        return Response(ret.dict)