from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from taggit.admin import Tag as TaggitTag
from .models import User, Tag, TagWithHits


admin.site.unregister(TaggitTag)


@admin.register(User)
class ProfileAdmin(UserAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Informações Pessoais",
            {"fields": ("first_name", "last_name", "apresentacao", "avatar")},
        ),
        ("Permissões", {"fields": ("is_superuser", "is_staff", "is_active")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "avatar",
                    "password",
                ),
            },
        ),
    )


class TaggedItemInline(admin.StackedInline):
    model = Tag


@admin.register(TagWithHits)
class TagAdmin(admin.ModelAdmin):
    inlines = [TaggedItemInline]
    list_display = ["name", "slug"]
    ordering = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ["name"]}
