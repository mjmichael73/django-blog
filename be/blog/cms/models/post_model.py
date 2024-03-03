from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post:
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADEl,
        related_name='cms_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )

    class Meta:
        ordering = ['-publish']  # From newest to oldest
        indexes = [
            models.Index(fields=['-publish'])
            # Hyphen before the field name to define the index in descending order (Not supported in MySQL)
        ]

    def __str__(self):
        return self.title
