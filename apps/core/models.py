import hashlib
from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.models import TagBase, GenericTaggedItemBase


def upload_directory_path(instance, filename):
    return 'users/{}/{}.{}'.format(
        instance.username, hashlib.sha224(filename.encode()).hexdigest(),
        filename.split(".")[-1:]
    )

class User(AbstractUser):
    apresentacao = models.CharField(max_length=120)
    avatar = models.ImageField(null=True, upload_to=upload_directory_path)


class TagWithHits(TagBase):
    hits = models.IntegerField(default=0)

    class Meta:
        ordering = ['hits']
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Tag(GenericTaggedItemBase):
    tag = models.ForeignKey(
        TagWithHits,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
    )
