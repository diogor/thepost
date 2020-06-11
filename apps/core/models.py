from django.db import models
from taggit.models import TagBase, GenericTaggedItemBase


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
