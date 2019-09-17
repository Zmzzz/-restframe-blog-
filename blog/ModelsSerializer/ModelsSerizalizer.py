from blog.models import *
from rest_framework import serializers
# 用户序列化：
class UserDetailSerializer(serializers.ModelSerializer):
        permissions = serializers.CharField(source='user.get_permissions_display')
        username = serializers.CharField(source='user.username')

        class Meta:
            model = UserDetail
            fields = ('nid', 'username', 'phone', 'permissions', 'avatars', 'user_avatars')


# 文章简单序列化
class ArticleSimpleSerializer(serializers.ModelSerializer):
    user=serializers.CharField(source='user.username')
    
    class Meta:
        model=Article
        fields=('nid','title','desc','create_time','up_count','down_count','comment_count','user')

# 文章详情序列化
class ArticleSerializer(serializers.ModelSerializer):
    article_user=serializers.CharField(source='user.username')
    category=serializers.SerializerMethodField()
    tags=serializers.SerializerMethodField()
    content=serializers.SerializerMethodField()
    # 评论
    comment=serializers.SerializerMethodField()
    class Meta:
        model=Article
        fields=('nid','title','desc','create_time','up_count','down_count','category','article_user','tags','content','comment')
    def get_category(self,obj):
        temp=[]
        for item in obj.category.all():
            temp.append({'category_id':item.nid,'category_name':item.title})
        return temp
    def get_tags(self,obj):
        temp=[]
        for item in obj.tags.all():
            temp.append({'tag_id':item.nid,'title':item.title})
        return temp
    def get_content(self,obj):
        temp=""
        for item in obj.articledetail_set.all():
            temp=item.content
        return temp
    def get_comment(self,obj):
        temp=[]
        for item in obj.comment_set.all():
            temp.append(
                            {
                                'comment_id':item.nid,
                                'comment_content':item.content,
                                'commentator':item.user.username,
                                'parent_id':item.parent_comment_id,
                                'comment_time':item.create_time,
                                'comment_status':item.is_delete
                                # 如果没有父评论，这个报错
                                  # 'parent_name':item.parent_comment.user.username,
                            })
        return temp
# 分类序列化
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['nid','title',]