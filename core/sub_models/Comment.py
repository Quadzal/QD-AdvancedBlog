from django.db import models
from django.core.exceptions import ValidationError
from .Post import Post




def censoring_banned_words(base_content):
    banned_words = ["bitch", "fuck", "fucking", "asshole",
                    "bastard", "ass", "chav", "cunt",
                    "dick", "slut"
    ]

    content = base_content.split(" ")
    result = ""
    for word in content:
        for banned_word in banned_words:
            if word.find(banned_word) > -1:
                word = " *******"

        result += word

    return result


class Comment(models.Model):
    author = models.ForeignKey("auth.user", related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    content = models.TextField(verbose_name="Content")
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)

    def existing_comments(self):
        return self.__class__.objects.filter(author=self.author, content=self.content, post=self.post)

    def save(self, *args, **kwargs):
        self.content = censoring_banned_words(self.content)

        if len(self.existing_comments()) > 0:
            raise ValidationError("Comment already exists.")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.content
