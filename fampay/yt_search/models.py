from django.db import models

class Videos(models.Model):

    id = models.AutoField(primary_key=True)

    title = models.CharField(
        null=True,
        blank=True,
        max_length=500
    )
    
    description = models.CharField(
        null=True,
        blank=True,
        max_length=10000
    )

    publishedAt = models.DateTimeField(
        null=True,
        blank=True,
    )

    thumbnailsUrls = models.URLField(
        null=True,
        blank=True,      
    )
    
    video_id = models.CharField(
        null=True,
        blank=False,
        max_length=200
    )


