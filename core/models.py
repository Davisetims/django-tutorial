from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class Course(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.FloatField(default=0)

    def __str__(self):
        return f'name:{self.name}, Price:{self.price}'


class Unit(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=10, null=True, blank=True)
    course = models.ForeignKey(Course,  on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f'unit code: {self.code}, name: {self.name}'

class User(AbstractUser):
    USERTYPES =[
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
        ('admin', 'Admin'),
    ]
    phone_regex = RegexValidator(
        regex=r'^\+\d{1,3}\d{9}$',
        message="Phone number must start with '+' followed by country code and 9 digits."
    )

    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    nationality = models.CharField(max_length=30, null=True, blank=True)
    national_id = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(
        max_length=13, 
        validators=[phone_regex],
        null=True, blank=True)
    email = models.EmailField()
    user_types = models.CharField(choices=USERTYPES, default='student')
    units = models.ManyToManyField('Unit', blank=True)
    password = models.CharField(max_length=1000)
    username = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.username

