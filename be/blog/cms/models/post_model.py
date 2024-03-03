from django.db import models
from django.utils import timezone


class Post:
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
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
