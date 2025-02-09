from django.db import models
from main.models import Tag, Media

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=60, blank=True)
    description = models.TextField(blank=True, null=True)
    term = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    tag = models.ManyToManyField(Tag, blank=True)
    media = models.ManyToManyField(Media, blank=True)
    start_at = models.DateTimeField(blank=True, null=True)
    finish_at = models.DateTimeField(blank=True, null=True)
    language = models.CharField(max_length=30, default='english')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id}, {self.title}'

class Lesson(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='lessons')
    topic = models.ManyToManyField(Tag)
    title = models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    content = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id}, {self.title}'

class Quizizz(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    content = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='quizizz_course')
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='quizizz_lesson')
    
    def __str__(self) -> str:
        return f'{self.id}, {self.lesson}'