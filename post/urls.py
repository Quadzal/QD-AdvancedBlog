from django.urls import path

from post.views import PopularPostsView, PostView, AddComment, favourite_post, favourite_comment

urlpatterns = [

    path('popular/posts', PopularPostsView.as_view(), name="popularPosts"),

    path('post/<str:slug>', PostView.as_view(), name="post"),

    path('add/comment', AddComment.as_view(), name="add_comment"),

    path('favourite/post', favourite_post),
    path('favourite/comment', favourite_comment),

]