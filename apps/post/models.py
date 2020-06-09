from django.db import models
from django.conf import settings


class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False,
                              on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    slug = models.SlugField("link", unique=True)
    texto = models.TextField()
    created_at = models.DateTimeField("criado", auto_now_add=True)
    modified_at = models.DateTimeField("modificado", auto_now=True)
