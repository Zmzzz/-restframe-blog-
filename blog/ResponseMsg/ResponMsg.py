class Response_msg(object):
    def __init__(self):
        self.data=None
        self.code=100
        self.error=None
    @property
    def dict(self):
        return self.__dict__