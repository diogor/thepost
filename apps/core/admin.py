from django.contrib import admin
from taggit.admin import Tag as TaggitTag
from .models import User, Tag, TagWithHits


admin.site.unregister(TaggitTag)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


class TaggedItemInline(admin.StackedInline):
    model = Tag


@admin.register(TagWithHits)
class TagAdmin(admin.ModelAdmin):
    inlines = [TaggedItemInline]
    list_display = ["name", "slug"]
    ordering = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ["name"]}
