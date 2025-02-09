from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=25)
    phone = PhoneNumberField(unique=True, null=True, blank=True)
    telegram_id = models.BigIntegerField(unique=True)
    search_history = models.TextField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    course_paid = models.ManyToManyField('course.Course', blank=True, related_name='users_paid')
    course_getted = models.ManyToManyField('course.Course', blank=True, related_name='users_getted')  
    lesson_complet = models.ManyToManyField('course.Lesson', blank=True, related_name='users_completed_lessons')    

    def __str__(self) -> str:
        return f'{self.id}, {self.name}'
    
class QuizizzAnswer(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='quizizz_answer')
    user_answer = models.CharField(max_length=255)
    answered_at = models.DateTimeField(auto_now_add=True)  
    quizizz = models.ForeignKey('course.Quizizz', on_delete=models.CASCADE, related_name='users_quizizz_answers')

    def __str__(self) -> str:
        return f'{self.name}, {self.user_answer}'