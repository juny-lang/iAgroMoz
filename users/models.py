from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone

# Create your models here.

class CustomUserManager (BaseUserManager):
    def create_user (self, email, password=None, **extra_fields):
        if not email:
            raise ValueError ('Email necessario')
        email=self.normalize_email(email)
        user= self.model (email=email, **extra_fields)
        user.set_password (password)
        user.save(using= self._db)
        return user
    def create_superuser(self, email,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        
        return self.create_user (email,password, **extra_fields)

class CustomUser (AbstractBaseUser, PermissionsMixin):
    email= models.EmailField(unique=True)
    nome= models.CharField( max_length=150, blank=True)
    telefone=models.IntegerField (unique=True)
    apelido=models.CharField(max_length=20)
    provincia = models.CharField(max_length=20)
    distrito = models.CharField(max_length= 20 )
    data_cadastro= models.DateField(default=timezone.now)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    def __str__(self):
        return self.email