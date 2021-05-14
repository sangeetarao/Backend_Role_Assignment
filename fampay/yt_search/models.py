from django.db import models

class Videos(models.Model):

    title = models.CharField(
        null=True,
        blank=True,
        max_length=500
    )

    description = models.CharField(
        null=True,
        blank=True,
        max_length=5000
    )

    publishedAt = models.DateTimeField()

    thumbnailsUrls = models.URLField()


