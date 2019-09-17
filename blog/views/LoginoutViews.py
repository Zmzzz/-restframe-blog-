from blog.ResponseMsg.ResponMsg import Response_msg
from rest_framework.response import Response
from django.contrib import auth
from rest_framework.views import APIView
class login_out(APIView):
    def get(self,request):
        ret=Response_msg()
        auth.logout(request)
        return Response(ret.dict)
