from django.contrib import admin
from .sub_models.Post import Post
from .sub_models.Category import Category
from .sub_models.Comment import Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)

