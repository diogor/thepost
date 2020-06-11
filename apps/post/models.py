import hashlib
from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from apps.core.models import Tag


def upload_directory_path(instance, filename):
    return 'posts/{}/{}.{}'.format(
        instance.slug, hashlib.sha224(filename.encode()).hexdigest(),
        filename.split(".")[-1:]
    )


class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False,
                              on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    lerd = models.CharField(max_length=300)
    slug = models.SlugField("link", unique=True)
    imagem_destaque = models.ImageField(upload_to=upload_directory_path)
    texto = models.TextField()
    tags = TaggableManager(through=Tag)
    destaque = models.BooleanField(default=False)
    created_at = models.DateTimeField("criado", auto_now_add=True)
    modified_at = models.DateTimeField("modificado", auto_now=True)

    class Meta:
        get_latest_by = '-created_at'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.titulo}, {self.autor.get_full_name()} - {self.created_at}"
