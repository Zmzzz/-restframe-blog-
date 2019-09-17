from   rest_framework.views import APIView
from  django.contrib import auth
from  blog.ResponseMsg.ResponMsg import Response_msg
from rest_framework.response import Response
from blog import models
from blog.Error.Error import MyError
from  blog.ModelsSerializer.ModelsSerizalizer import UserDetailSerializer

from django.shortcuts import render
class login(APIView):

    def post(self,request):
        ret=Response_msg()
        try:
            username=request.data.get('username')
            password=request.data.get('password')
            # valid_code=request.data.get('valid_code')
            # if valid_code.upper() != request.session.get('valid_code'):
            #     raise MyError('300','验证码不正确')
            user_isexit=models.UserInfo.objects.filter(username=username)
            if not user_isexit :
                raise MyError('300','账户不正确')
            user=auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
            else:
                raise MyError('300','密码不正确')
            #登录成功，返回用户数据
            user_obj=models.UserInfo.objects.filter(username=username).first()
            user_detail=models.UserDetail.objects.filter(user=user_obj).first()
            us=UserDetailSerializer(user_detail)
            ret.data=us.data
        except MyError as e:
                ret.code=e.code
                ret.error=e.msg
        # except Exception as e:
        #         ret.code=200
        #         ret.error='数据库异常'
        return Response(ret.dict)

