from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}
    list_display = ["titulo", "slug", "created_at", "modified_at"]
    list_filter = ("created_at", "modified_at")
    search_fields = (
        "titulo",
        "texto",
        "autor__username",
        "autor__first_name",
        "autor__last_name",
    )

    def save_model(self, request, obj, form, change):
        if not obj.autor_id:
            obj.autor = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)

    def get_list_display(self, request):
        if request.user.is_superuser:
            return self.list_display + ["autor"]
        return self.list_display
