""" Modules... """
from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from .views import (
    HomeView,
    PostView,
    AuthorPostsView,
    SearchPostsView,
    SearchPostsWithTagView,
    AddComment,
    CategoryPostsView,
    favourite_post,
    favourite_comment,

)
from .forms import CustomUserCreationForm

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    
    path('search/', SearchPostsView.as_view()),

    path('post/<str:slug>', PostView.as_view(), name="post"),

    path('tag/<str:tag>', SearchPostsWithTagView.as_view(), name="tag_posts"),

    path('author/<str:username>', AuthorPostsView.as_view(), name="author"),

    path('add/comment', AddComment.as_view(), name="add_comment"),
    path('category/<str:category_name>', CategoryPostsView.as_view(), name="category"),

    path('favourite/post', favourite_post),
    path('favourite/comment', favourite_comment),

    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True), name="login"),

    path('accounts/register/', CreateView.as_view(
        form_class=CustomUserCreationForm, 
        template_name="registration/register.html", 
        success_url="/"), 
        name="register"
    ),

    re_path(r'^password_reset/', auth_views.password_reset, name='password_reset'),
    re_path(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]