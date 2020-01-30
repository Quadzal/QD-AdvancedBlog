from django.db import models
from .Category import Category
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

class Post(models.Model):
    author = models.ForeignKey("auth.user", related_name="posts", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)

    title = models.CharField(max_length=50, verbose_name="Title", unique=True, null=True, blank=False)
    content = RichTextField(verbose_name="Content", unique=True)
    description = models.TextField(verbose_name="Description", help_text="Meta Description Tag.", max_length=500,
                                   null=True, blank=True)

    image = models.ImageField(verbose_name="Image", null=True, blank=False)
    tags = models.CharField(max_length=999, verbose_name="Tags", null=False, blank=False,
                            help_text="Eg:django,django1,django2,...")

    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    slug = models.SlugField(editable=False)

    total_views = models.IntegerField(default=0)

    class Meta:
        ordering = ["created_date"]

    def tags_list(self):
        return self.tags.split(",")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)