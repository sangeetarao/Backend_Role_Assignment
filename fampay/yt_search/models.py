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
        max_length=5000
    )

    publishedAt = models.DateTimeField()

    thumbnailsUrls = models.URLField()
    
    video_id = models.CharField(
        null=True,
        blank=False,
        max_length=200
    )


