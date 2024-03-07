from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cms_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )

    objects = models.Manager()  # The default manager
    published = PublishedManager()  # Our Custom manager

    class Meta:
        ordering = ['-publish']  # From newest to oldest
        indexes = [
            models.Index(fields=['-publish'])
            # Hyphen before the field name to define the index in descending order (Not supported in MySQL)
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'cms:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )
