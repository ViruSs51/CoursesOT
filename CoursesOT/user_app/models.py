from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, telegram_id, username=None, first_name=None, last_name=None, password=None, **extra_fields):
        if not telegram_id:
            raise ValueError("The telegram_id field must be set")
        
        user = self.model(username=username, telegram_id=telegram_id, first_name=first_name, last_name=last_name, **extra_fields)
        
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(username, password=password, **extra_fields)


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    username = models.CharField(max_length=25, null=True)
    phone = PhoneNumberField(unique=True, null=True, blank=True)
    telegram_id = models.BigIntegerField(unique=True)
    search_history = models.TextField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    course_paid = models.ManyToManyField('course.Course', blank=True, related_name='users_paid')
    course_getted = models.ManyToManyField('course.Course', blank=True, related_name='users_getted')  
    lesson_complet = models.ManyToManyField('course.Lesson', blank=True, related_name='users_completed_lessons')    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'{self.id}, {self.username}, {self.first_name}, {self.last_name}'
    
class QuizizzAnswer(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='quizizz_answer')
    user_answer = models.CharField(max_length=255)
    answered_at = models.DateTimeField(auto_now_add=True)  
    quizizz = models.ForeignKey('course.Quizizz', on_delete=models.CASCADE, related_name='users_quizizz_answers')

    def __str__(self) -> str:
        return f'{self.name}, {self.user_answer}'