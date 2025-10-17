from django.contrib import admin

from . import models
from.models import Article,Category,Comment,Message,Like
# Register your models here.

class FilterByTitle(admin.SimpleListFilter):
    title = " کلید های پرتکرار"
    parameter_name = "title"

    def lookups(self, request, model_admin):
        return (
            ("django","DJANGO"),
            ("python","PYTHON"),
    )

    def queryset(self, request, queryset):
        if self.value() :
            return queryset.filter(title__icontains=self.value())

class CommentInline(admin.TabularInline):
    model = models.Comment

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("__str__","author","views","status","published","show_image")
    list_editable = ("status",)
    # list_filter = ("published", FilterByTitle)
    inlines = (CommentInline,)
    search_fields = ("title","body")


admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Like)
