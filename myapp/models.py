from django.db import models
from django.utils import timezone


class Profile(models.Model):
    """Example model for user profile with image upload."""
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True,
        help_text='Upload a profile picture'
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Document(models.Model):
    """Example model for document uploads."""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(
        upload_to='documents/%Y/%m/%d/',
        help_text='Upload a document file'
    )
    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title


class Gallery(models.Model):
    """Example model for image gallery."""
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='gallery/%Y/%m/',
        help_text='Upload gallery image'
    )
    caption = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return self.title
