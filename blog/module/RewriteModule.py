# 重写频率异常抛出错误
import math
from rest_framework.exceptions import APIException
class Throttled(APIException):
    def __init__(self,wait=None):
        if wait is not None:
            wait = math.ceil(wait)
        self.wait = wait
        detail={
                "data":"",
                "code": 105,
                "error": "您的访问频率过快，距离下次需要等待{0}秒".format(self.wait)
        }
        super(Throttled, self).__init__(detail, None)