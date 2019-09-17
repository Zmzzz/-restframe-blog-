from blog import models
from rest_framework import viewsets
from rest_framework.response import Response
from blog.module.RewriteModule import Throttled
from blog.module.RestFrameworkModule import MyThrottle, MyPagePagination
from blog.ModelsSerializer.ModelsSerizalizer import ArticleSimpleSerializer
from blog.ResponseMsg.ResponMsg import Response_msg
from django.db.models import Avg, Sum, Max, Min, Count

class blog_home(viewsets.ModelViewSet):
    # 频率认证
    throttle_classes = [MyThrottle]
    def throttled(self, request, wait):
        raise  Throttled(wait)
    queryset = models.Article.objects.all()
    serializer_class = ArticleSimpleSerializer
    # 重写List方法，个人感觉Model.ViewSet没有用了如果只是一个查询
    def list(self, request, *args, **kwargs):
        ret=Response_msg()
        try:
            book_list = models.Article.objects.all().order_by('create_time')
            mp = MyPagePagination()# 实例化一个分页器对象
            article_page = mp.paginate_queryset(book_list, request, self)
            data= ArticleSimpleSerializer(article_page, many=True, context={"request": request})
            # 获取全部的博客分类，每个分类下的文章数
            blog_category = models.Category.objects.annotate(category_count=Count('article__nid')).values()

            ret.data={
                            'all_article_list':data.data,
                            'all_category':blog_category
                        }
        except Exception as e:
            ret.code='200'
            ret.error='数据库异常'
        return Response(ret.dict)


