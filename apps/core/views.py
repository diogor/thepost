from django.views.generic import TemplateView
from apps.post.models import Post
from .models import TagWithHits


class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        destaques = Post.objects.filter(destaque=True)[:2]
        tags = TagWithHits.objects.all()[:10]

        def destaque_tags():
            for t in tags[:3]:
                try:
                    post = Post.objects.filter(
                        tags__slug=t.slug
                    ).exclude(id__in=[p.id for p in destaques]).latest()
                    yield post
                except Post.DoesNotExist:
                    pass

        context.update({
            'destaques': destaques,
            'tags': tags,
            'destaque_tags': [p for p in destaque_tags()] 
        })
        return context
