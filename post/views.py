from django.core.exceptions import ValidationError
from django.http import JsonResponse

from django.views.generic import ListView, DetailView, CreateView
from core.sub_models.Comment import Comment
from post.models import Post
from user.models import UserProfile


class HomeMixin:
    context_object_name = "posts"
    template_name       = "home/home.html"
    paginate_by         = 10


class PopularPostsView(HomeMixin, ListView):
    queryset = Post.objects.all().order_by('-number_of_favourite')


class PostView(DetailView):
    template_name = 'home/post.html'
    context_object_name = "post"

    def get_object(self):
        return Post.objects.get(slug=self.kwargs["slug"])


class AddComment(CreateView):
    model = Comment
    fields = ("content", )
    template_name = '_layouts/_commentForm.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=self.request.POST.get("post"))
        try:
            comment = form.save()
            return JsonResponse({"comment": {"author": str(comment.author), "created_date": comment.created_date}})
        except ValidationError as err:
            return JsonResponse({"error": err.message})


def favourite_post(request):

    user = UserProfile.objects.get(user__username=request.POST.get("user"))

    post = Post.objects.get(title=request.POST.get("post_title"))

    try:
        user_favourite_post = user.favourite_posts.get(title=post.title)
        user.favourite_posts.remove(user_favourite_post)
        post.number_of_favourite -= 1
        post.save()

    except Post.DoesNotExist:
        user.favourite_posts.add(post)
        post.number_of_favourite += 1
        post.save()

    return JsonResponse({"code": "success"})


def favourite_comment(request):

    user = UserProfile.objects.get(user__username=request.POST.get("user"))
    comment = Comment.objects.get(pk=request.POST.get("comment_id"))

    try:
        user_favourite_comment = user.favourite_comments.get(pk=comment.pk)
        user.favourite_comments.remove(user_favourite_comment)

    except Comment.DoesNotExist:
        user.favourite_comments.add(comment)

    return JsonResponse({"code":"success"})
