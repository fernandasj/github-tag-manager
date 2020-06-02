import uuid
from django.conf import settings
from django.db import models


class Tag(models.Model):
    id_tag = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        'Repository name',
        max_length=100
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Repository(models.Model):
    id_repository = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        'Repository name',
        max_length=100
    )

    description = models.CharField(
        'Repository description',
        max_length=100
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name='tag',
        related_name='repositories',
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Repository'
        verbose_name_plural = 'Repositories'
