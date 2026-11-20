"""
accounts/models.py
Custom User model + UserProfile (farmer details) for Sugar Factory Booking System
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    """Custom manager for email-based authentication (replaces username)."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model — email is the login identifier.
    """
    email = models.EmailField(unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def get_full_name(self):
        profile = getattr(self, 'profile', None)
        if profile:
            return f"{profile.fname} {profile.lname}".strip()
        return self.email


class UserProfile(models.Model):
    """
    Farmer/User profile details.
    id, fname, lname, email, phone, ifsc, acc, user_id.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        db_column='user_id'
    )
    fname = models.CharField(max_length=100, verbose_name='First Name')
    lname = models.CharField(max_length=100, verbose_name='Last Name')
    email = models.EmailField(verbose_name='Contact Email')
    phone = models.CharField(max_length=15, verbose_name='Phone Number')
    ifsc = models.CharField(max_length=20, blank=True, verbose_name='IFSC Code')
    acc = models.CharField(max_length=30, blank=True, verbose_name='Account Number')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_info'
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.user.email})"
