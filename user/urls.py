""" Modules... """
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

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
    path('', include("django.contrib.auth.urls"))
]