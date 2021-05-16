from django.db import models

class Videos(models.Model):

    title = models.CharField(
        null=True,
        blank=True,
        max_length=500
    )
    id = models.AutoField(primary_key=True)

    description = models.CharField(
        null=True,
        blank=True,
        max_length=10000
    )

    publishedAt = models.DateTimeField()

    thumbnailsUrls = models.URLField()
    
    video_id = models.CharField(
        null=True,
        blank=False,
        max_length=200
    )
    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )


