from django.conf.urls import url
from blog.views.HomeViews import blog_home
from blog.views.ArticleViews import article_detail
from  blog.views.UserArticleViews import user_article
from blog.views.CommentViews import comment
from blog.views.UpDownViews import up_down
urlpatterns = [
    # 博客主页

    url(r'^index/$',blog_home.as_view({'get': 'list'}),name='blog_home'),
    # 查看用户的某一篇文章
    url(r'^(?P<username>\w+)/article/(?P<pk>\d+)/$',article_detail.as_view({'get':'list'}),name='article_detail'),
    # 更新文章
    url(r'^update_article/(?P<username>\w+)/(?P<pk>\d+)/$',article_detail.as_view({'put':'update','get':'list'}),name='update_article'),
    # 增加文章
    url(r'^add_article/(?P<username>\w+)/$',article_detail.as_view({'post':'create'}),name  ='create_article'),
    
    # 查看用户的所有文章
    url(r'^(?P<username>\w+)/article/$',user_article.as_view({'get':'list'}),name='get_user_article'),
    # 用户删除文章
    url(r'^delete_article/(?P<username>\w+)/(?P<pk>\d+)/$',article_detail.as_view({'delete':'destroy'}),name='delete_article'),
    # 用户删除评论，，用户名，文章id，评论id
    url(r'^delete_comment/(?P<username>\w+)/(?P<article_pk>\d+)/(?P<comment_pk>\d+)/$',comment.as_view({'delete':'destroy'})),
    # 用户添加评论
    url(r'^add_comment/$',comment.as_view({'post':'create'})),

    # 用户点赞或者踩
    url(r'^up_down/$',up_down.as_view(),name='up_down')

]



