""" Modules... """
from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views

from .views import (
    ProfileView,
    FavouritePosts,
    FavouriteComments,
)

from .forms import CustomUserCreationForm


urlpatterns = [

    path('profile/favourites/posts', FavouritePosts.as_view(), name="favourite_posts"),
    path('profile/favourites/comments', FavouriteComments.as_view(), name="favourite_comments"),
    path('profile/', ProfileView.as_view(), name="profile"),

    path('login/', LoginView.as_view(redirect_authenticated_user=True), name="login"),

    path('register/', CreateView.as_view(
        form_class=CustomUserCreationForm,
        template_name="registration/register.html",
        success_url="/"),
         name="register"
         ),

    path('password_reset/', auth_views.password_reset, name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout")
]