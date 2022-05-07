from distutils.command.upload import upload
from django.db import models

# Create your models here.
import uuid
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.forms import ValidationError
from clubs.models import *

class UserManager(BaseUserManager):

    def create_user(self,email,password=None):
        if email is not None:
            user = self.model(email=email,)
        else:
            raise ValidationError("Credentials missing")
        if password is not None:
            user.set_password(password)
        else:
            user.set_password(email)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None,):
        user = self.create_user(email,password)
        user.save(using=self._db)
        user.is_superuser = True
        user.is_staff = True
        user.is_active=True
        user.is_club_head=True
        user.save(using=self._db)


class User(AbstractBaseUser,PermissionsMixin):
    uid = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    email = models.EmailField(max_length=150,unique=True)
    is_club_head = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ('name','year','phone','branch','addminsion_number')

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.email}-{self.uid}'


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    year = models.IntegerField(null=True)
    phone = models.CharField(max_length=10)
    addminsion_number = models.CharField(max_length=100,unique=True)
    branch = models.CharField(max_length=20)
    club = models.ForeignKey(Club,on_delete=models.CASCADE,blank=True,null=True)
    profile_pics = models.ImageField(upload_to="profilepics",default="default.jpg")

    def __str__(self):
        return f'{self.user.email}-{self.addminsion_number}'