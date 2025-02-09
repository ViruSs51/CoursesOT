from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
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
    path = models.CharField(max_length=1000)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id}, {self.title}'