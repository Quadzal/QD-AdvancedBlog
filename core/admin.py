from django.contrib import admin
from .sub_models.Category import Category
from .sub_models.Comment import Comment
from .sub_models.Complaints import Complaints
# Register your models here.

admin.site.register(Category)
admin.site.register(Comment)


class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ["complainant", "subject", "status"]


admin.site.register(Complaints, ComplaintsAdmin)
