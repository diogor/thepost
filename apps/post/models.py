from django.db import models
from django.conf import settings

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)
