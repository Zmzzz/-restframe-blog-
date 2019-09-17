from  rest_framework.response import Response
from rest_framework.views import APIView
from  blog.ResponseMsg.ResponMsg import Response_msg
from blog.Error.Error import MyError
from blog import models
from blog.module.RestFrameworkModule import MyThrottle
from blog.module.RewriteModule import Throttled
from django.db import transaction

class register(APIView):
    throttle_classes = [MyThrottle]
    #重写抛出异常
    def throttled(self, request, wait):
        raise  Throttled(wait)


    def post(self, request):
        ret = Response_msg()
        username = request.data.get('username')
        password = request.data.get('password')
        phone = request.data.get('phone')
        try:
            # 判断用户是否已存在
            user_isexist = models.UserInfo.objects.filter(username=username)
            if user_isexist:
                raise MyError(101, '用户已存在')
            # 判断手机号是否存在
            phone_isexist = models.UserDetail.objects.filter(phone=phone)
            if phone_isexist:
                raise MyError(102, '手机号已存在')
            # 获取传过来的文件
            avatars=request.FILES.get('avatars')
            with transaction.atomic():
                user=models.UserInfo.objects.create_user(username=username, password=password)
                if not avatars:
                    models.UserDetail.objects.create(user=user,phone=phone)
                else:
                    models.UserDetail.objects.create(user=user,phone=phone,avatars=avatars,user_avatars=1)
                
            # # 创建每个用户专属的token
            # import uuid
            # token = uuid.uuid1()
            # models.Token.objects.create(token=token, user=user)
        except MyError as e:
            ret.code = e.code
            ret.error = e.msg
        # except Exception as  e:
        #     ret.code = 200
        #     ret.error = '数据库异常'
        return Response(ret.dict)

    
        