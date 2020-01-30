from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from core.sub_models.Post import Post
from core.sub_models.Comment import Comment

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name="profile")

    profile_image = models.ImageField(upload_to="profile_images/", verbose_name="Profile Image", null=True, blank=True)

    favourite_posts = models.ManyToManyField(Post)
    favourite_comments = models.ManyToManyField(Comment)

    def image_url(self):
        base_image_path = "/media/"
        if self.profile_image:
            return base_image_path + self.profile_image.name

        default_image_path = base_image_path + "default_profile_images/{0}.png".format(self.user.username[0])

        return default_image_path


    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, User)