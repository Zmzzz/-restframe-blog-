from rest_framework.views import APIView
from django.db import transaction
from blog import models
from django.db.models import F
from blog.ResponseMsg.ResponMsg import Response_msg
from rest_framework.response import Response
class up_down(APIView):
    def post(self,request):
        ret=Response_msg()
        try:
            # 获取用户，文章，点赞还是踩
            user_id=request.data.get('user_id')
            article_id=request.data.get('article_id')
            is_up=request.data.get('is_up')
            # 判断是点赞还是踩
            # 点赞
            with transaction.atomic():
                if is_up:
                    # 创建点赞表、
                    models.ArticleUpDown.objects.create(user_id=user_id,article_id=article_id)
                    models.Article.objects.filter(nid=article_id).update(up_count=F("up_count")+1)
                else:
                    models.ArticleUpDown.objects.create(user_id=user_id, article_id=article_id,is_up=False)
                    models.Article.objects.filter(nid=article_id).update(up_count=F("down_count") + 1)

        except Exception as e:
            ret.code=300
            ret.error='已经进行过点赞或者踩了'
        return Response(ret.dict)
