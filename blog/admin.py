from django.contrib import admin

# Register your models here.
from blog.models import *

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(ArticleDetail)
admin.site.register(ArticleUpDown)
admin.site.register(Comment)
admin.site.register(Category)
