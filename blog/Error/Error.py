#自定义异常
class MyError(Exception):
    def __init__(self, code=None,msg=None):
        self.code=code
        self.msg = msg
