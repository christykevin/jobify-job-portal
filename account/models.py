from django.contrib.auth.models import AbstractUser
from django.db import models

from account.managers import CustomUserManager

JOB_TYPE = (
    ('M', "Male"),
    ('F', "Female"),

)

ROLE = (
    ('employer', "Employer"),
    ('employee', "Employee"),
)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    role = models.CharField(choices=ROLE,  max_length=10)
    gender = models.CharField(choices=JOB_TYPE, max_length=1)
    location = models.CharField( max_length=100)
    skills = models.CharField( max_length=100)
    MobileNumber = models.CharField( max_length=100)
    Xth = models.CharField( max_length=200)
    XIIth = models.CharField( max_length=200)
    UG = models.CharField( max_length=200)
    PG = models.CharField( max_length=200)
    Experience = models.CharField( max_length=200)
    AcademicProjects = models.CharField( max_length=200) 




    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name+ ' ' + self.last_name
    objects = CustomUserManager()
