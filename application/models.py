from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
# Create your models here.





class User(AbstractUser):
    
    class Type(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        TEACHER = 'TEACHER', 'Teacher'
        DIRECTOR = 'DIRECTOR', 'Director'

    type = models.CharField(_("type"), max_length=50, choices=Type.choices, default=Type.STUDENT)
    name = models.CharField(_("Name of User"), max_length=100, blank=True, null=True)

class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Type.STUDENT)    


class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Type.TEACHER)    


class DirectorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Type.DIRECTOR)    

class Student(User):

    objects = StudentManager()
    class Meta:
        proxy = True


    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Type.STUDENT
            return super().save(*args, **kwargs)    

    def student(self):
        return 'learning'        


class Teacher(User):

    objects = TeacherManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Type.TEACHER
            return super().save(*args, **kwargs)  


    def teach(self):
        return "He is teaching"           


class Director(User):

    objects = DirectorManager()
    class Meta:
        proxy = True   


    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Type.DIRECTOR
            return super().save(*args, **kwargs)     

    def director(self):
        return 'doing some stuff'                             
    
