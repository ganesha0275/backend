from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    mob_no   = models.CharField(max_length = 10, unique=True)
    address  = models.TextField()
    post     = models.CharField(max_length = 30)
    district = models.CharField(max_length = 30)
    taluka   =  models.CharField(max_length = 30)
    
    USERNAME_FIELD = 'mob_no'

    class Meta:
        db_table = 'auth_user'
