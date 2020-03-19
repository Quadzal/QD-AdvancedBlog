from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView
from .forms import ProfileForm, CustomUserChangeForm
from .models import UserProfile


class ProfileView(UpdateView):
    template_name = "home/profile.html"
    form_class = ProfileForm
    success_url = "/"

    def form_valid(self, form):
        user_change = CustomUserChangeForm(self.request.POST, instance=self.request.user)
        if user_change.is_valid():
            user_change.save()
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_change_form"] = CustomUserChangeForm(instance=self.request.user)
        return context

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)


class FavouritePosts(LoginRequiredMixin, ListView):
    login_url = "/accounts/login"
    context_object_name = "posts"
    template_name = "home/home.html"
    paginate_by = 10

    def get_queryset(self):
        user = UserProfile.objects.prefetch_related("favourite_posts").get(user=self.request.user)

        if user:
            favourite_posts = user.favourite_posts.all()
            return favourite_posts


class FavouriteComments(LoginRequiredMixin, ListView):
    login_url = "/accounts/login"
    context_object_name = "comments"
    template_name = "home/favourite_comments.html"
    paginate_by = 10

    def get_queryset(self):
        user = UserProfile.objects.prefetch_related("favourite_comments").get(user=self.request.user)

        if user:
            favourite_posts = user.favourite_comments.all()
            return favourite_posts
