from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class AdminManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        admin = self.model(username=username, email=email, **extra_fields)
        admin.set_password(password)
        admin.save(using=self._db)
        return admin

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class Admin(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=255)
    admin_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = AdminManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'admin_number', 'full_name']

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_superuser

class StudentManager(BaseUserManager):
    def create_user(self, email, reference_number, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        student = self.model(email=email, reference_number=reference_number, **extra_fields)
        student.set_password(password)
        student.save(using=self._db)
        return student

    def create_superuser(self, email, reference_number, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(email, reference_number, password, **extra_fields)

class DepartmentClearance(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    id = models.AutoField(primary_key=True)
    clearance_start_date = models.DateField()
    description = models.TextField()
    department = models.ForeignKey(Department, to_field='code', on_delete=models.CASCADE, related_name='clearances')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='clearances')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_cleared')

    def __str__(self):
        return f"{self.department.name} - {self.user.full_name} - {self.status}"
    
class Student(AbstractBaseUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    reference_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    level = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    departmentClearance = models.ForeignKey(DepartmentClearance, blank=True, on_delete=models.CASCADE, related_name='students')

    objects = StudentManager()

    USERNAME_FIELD = 'reference_number'
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return self.full_name

    @property
    def is_staff(self):
        return self.is_admin

