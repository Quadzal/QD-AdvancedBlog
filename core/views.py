from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.views.generic import ListView, DetailView, CreateView
from .sub_models.Post import Post
from .sub_models.Category import Category
from .sub_models.Comment import Comment
from user.models import UserProfile


class HomeMixin:
    context_object_name = "posts"
    template_name       = "home/home.html"
    paginate_by         = 10


class MyLoginRequiredMixin(LoginRequiredMixin):
    login_url = "/accounts/login"


class HomeView(HomeMixin, ListView):
    queryset = Post.objects.select_related("author", "category").all()


class PostView(DetailView):
    template_name       = "home/post.html"
    context_object_name = "post"
    
    def get_object(self):
        return Post.objects.get(slug=self.kwargs["slug"])


class AuthorPostsView(HomeMixin, ListView):
    
    def get_queryset(self, *args, **kwargs):
        author = User\
            .objects\
            .prefetch_related("posts")\
            .get(username=self.kwargs["username"])

        author_posts = author.posts.all()
        return author_posts


class SearchPostsView(HomeMixin, ListView):

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        posts = Post\
            .objects\
            .select_related("author", "category")\
            .filter(title__contains=query)
        return posts


class CategoryPostsView(HomeMixin, ListView):

    def get_queryset(self, *args, **kwargs):
        category = Category\
            .objects\
            .prefetch_related("posts")\
            .get(slug__iexact=self.kwargs["category_name"])

        category_posts = category.posts.all()
        return category_posts


class SearchPostsWithTagView(HomeMixin, ListView):

    def get_queryset(self, *args, **kwargs):
        tag = self.kwargs["tag"]
        posts = Post\
            .objects\
            .select_related("author", "category")\
            .all()

        filtered_posts = [filtered_post for filtered_post in posts if tag in filtered_post.tags.split(",")]
        return filtered_posts


class AddComment(CreateView):
    model = Comment
    fields = ("content", )
    template_name = "_layouts/_commentForm.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=self.request.POST.get("post"))
        try:
            comment = form.save()
            return JsonResponse({"comment":{"author":str(comment.author), "created_date":comment.created_date}})
        except ValidationError as err:
            return JsonResponse({"error": err.message})


def favourite_post(request):

    user = UserProfile\
        .objects\
        .prefetch_related("favourite_posts")\
        .get(user__username=request.POST.get("user"))

    post = Post.objects.get(title=request.POST.get("post_title"))

    try:
        user_favourite_post = user.favourite_posts.get(title=post.title)
        user.favourite_posts.remove(user_favourite_post)

    except Post.DoesNotExist:
        user.favourite_posts.add(post)

    return JsonResponse({"code":"success"})


def favourite_comment(request):

    user = UserProfile.objects.prefetch_related("favourite_comments").get(user__username=request.POST.get("user"))
    comment = Comment.objects.get(pk=request.POST.get("comment_id"))

    try:
        user_favourite_comment = user.favourite_comments.get(pk=comment.pk)
        user.favourite_comments.remove(user_favourite_comment)

    except Comment.DoesNotExist:
        user.favourite_comments.add(comment)

    return JsonResponse({"code":"success"})
