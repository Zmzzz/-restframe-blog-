# 频率组件
from rest_framework.throttling import SimpleRateThrottle
class MyThrottle(SimpleRateThrottle):
    scope = "visit_rate"  # 这个值决定了在配置时使用那个变量描述限制的频率
    def get_cache_key(self, request, view):  # 这个方法也是必须要有
        return self.get_ident(request)


# 分页组件
from rest_framework.pagination import PageNumberPagination
class MyPagePagination(PageNumberPagination):
    # 定义每一页显示的数据个数
    page_size = 2
    # 定义查询参数  ?page=1&size=2
    page_size_query_param = 'size'
    # 关于页码  ?page=1 想用p就写p
    page_query_param = 'p'
    # 最大返回数据的个数
    max_page_size = 5