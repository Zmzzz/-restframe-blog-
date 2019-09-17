from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  viewsets
from  blog.module.RestFrameworkModule import MyPagePagination,MyThrottle
from blog.module.RewriteModule import Throttled
from  blog import models
from blog.Error.Error import MyError
from  blog.ModelsSerializer.ModelsSerizalizer import ArticleSimpleSerializer
from blog.ResponseMsg.ResponMsg import Response_msg
class user_article(viewsets.ViewSetMixin,APIView):
    throttle_classes = [MyThrottle]
    def throttled(self, request, wait):
        raise  Throttled(wait)
    def list(self,request,*args,**kwargs):
        ret = Response_msg()
        try:
            username=kwargs.get('username')
            user=models.UserInfo.objects.filter(username=username).first()
            if not user:
                raise MyError('300','找不到这个作者')
            article_list=models.Article.objects.filter(user=user).order_by('nid')
            mp=MyPagePagination()
            article_page = mp.paginate_queryset(article_list, request, self)
            data = ArticleSimpleSerializer(article_page, many=True, context={"request": request})
            ret.data=data.data
        except MyError as  e:
            ret.code=e.code
            ret.error=e.msg
        # except Exception as e:
        #     ret.code='200'
        #     ret.error='数据库异常'
        return  Response(ret.dict)
        
    
        

