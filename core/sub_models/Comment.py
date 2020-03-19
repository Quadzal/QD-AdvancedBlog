from django.db import models
from django.core.exceptions import ValidationError



class Comment(models.Model):
    author = models.ForeignKey("auth.user", related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name="comments")

    content = models.TextField(verbose_name="Content")
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)

    def existing_comments(self):
        """
            Eğer Yeni Gelen Yorum Daha ÖNceden Var İse Onu Döndürür.
        :return: existing comment
        """
        return self.__class__.objects.filter(author=self.author, content=self.content, post=self.post)

    def save(self, *args, **kwargs):
        if len(self.existing_comments()) > 0:
            raise ValidationError("Comment already exists.")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.content
