import uuid
from django.db import models
import uuid


def media_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4().hex}.{ext}'

    return f'{instance.type}/{new_filename}'

# Create your models here.
class Tag(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    usage_count = models.PositiveBigIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.id}, {self.title}'

class Media(models.Model):
    MEDIA_TYPES = [
        ('image', 'image'),
        ('video', 'video'),
        ('audio', 'audio'),
        ('file', 'file'),
    ]

    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=60, blank=True, null=True)
    type = models.CharField(max_length=15, choices=MEDIA_TYPES, default='image')
    file = models.FileField(upload_to=media_upload_path)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id}, {self.title}'