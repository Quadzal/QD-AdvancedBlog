from django.db import models

choices = (
    ("p", "processing"),
    ("ps", "processed"),
    ("cps", "complaint process succeed"),
)


class Complaints(models.Model):
    complainant = models.CharField(max_length=18,) #Şikayet Eden
    subject = models.CharField(max_length=120,) # Şikayet Konusu
    post_url = models.URLField(default="") # Şikayet Edilen Gönderi
    content = models.TextField(max_length=9999, default="") # Şikayet İçeriği
    status = models.CharField(
        max_length=32,
        choices=choices,
        default="p"
    )
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.subject
