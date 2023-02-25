from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        if not phone:
            raise TypeError('Username did not come')
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        if not password:
            raise TypeError('Password did not come')
        user = self.create_user(phone, password, **kwargs)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=14, unique=True, db_index=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone


class VerifyPhone(models.Model):
    class Meta:
        verbose_name = "Telefon raqamni tasdiqlash"
        verbose_name_plural = "Telefon raqam tasdiqlash"

    phone = models.CharField(max_length=15, verbose_name="Phone number")
    code = models.CharField(max_length=10, verbose_name="Code")

    def __str__(self):
        return self.phone
