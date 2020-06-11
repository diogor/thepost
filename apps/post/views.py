from django.views.generic import DetailView
from .models import Post


class PostDetail(DetailView):
    template_name = "post.html"
    model = Post
