import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self,name,email,password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_owner", False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, email, password, **extra_fields)
    
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_owner', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True, default='')
    phone_number = models.CharField(max_length=40, blank=True, null=True,)
    first_name = models.CharField(max_length=255,blank=True, null=True,)
    last_name = models.CharField(max_length=255,blank=True, null=True,)
  
    user_avatar = models.ImageField(upload_to='user_avatars', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_image(self):
        if self.user_avatar:
            return self.user_avatar.url
        return ''

    @property
    def role(self):
        if self.is_superuser:
            return 'superuser'
        if self.is_owner:
            return 'owner'
        return 'user'
        
