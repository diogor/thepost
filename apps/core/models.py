from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.models import TagBase, GenericTaggedItemBase


class User(AbstractUser):
    apresentacao = models.CharField(max_length=120)


class TagWithHits(TagBase):
    hits = models.IntegerField(default=0)

    class Meta:
        ordering = ['hits']


class Tag(GenericTaggedItemBase):
    tag = models.ForeignKey(
        TagWithHits,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
    )
