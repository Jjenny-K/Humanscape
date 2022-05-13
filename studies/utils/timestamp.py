from django.db import models


class TimestampZone(models.Model):
    """
        작성자 : 강정희, 김채욱
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
