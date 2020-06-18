from django.views.generic import DetailView, ListView
from .models import Post


class PostDetail(DetailView):
    template_name = "post.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        posts = Post.objects.filter(
            tags__slug__in=[t.slug for t in post.tags.all()]
        ).exclude(id=post.id)[:3]
        
        context.update({
            'related_posts': posts
        })
        return context


class PostListTag(ListView):
    template_name = "posts_tag.html"
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.kwargs.get('tag')
        if tag:
            queryset = queryset.filter(tags__slug=tag)
        return queryset
