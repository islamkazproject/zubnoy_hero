from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models


# Менеджер пользователей
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


# Модель пользователя
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('doctor', 'Врач'),
        ('registrar', 'Регистратор'),
        ('client', 'Клиент'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    groups = models.ManyToManyField(Group, related_name='zubnoy_users')
    user_permissions = models.ManyToManyField(Permission, related_name='zubnoy_users')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'


# Дополнительная информация для врачей
class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='Врач:')
    def __str__(self):
        return f'{self.user}'

# Дополнительная информация для регистраторов
class RegistrarProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='Регистратор:')
    def __str__(self):
        return f'{self.user}'


# Дополнительная информация для клиентов
class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='Пользователь:')

    def __str__(self):
        return f'{self.user}'


class Service(models.Model):
    name = models.TextField(max_length=255, verbose_name='Название услуги:')
    price = models.PositiveSmallIntegerField(default=0, verbose_name='Стоимость услуги:')

    def __str__(self):
        return f'{self.name} {self.price}'


class Schedule(models.Model):
    doctor_id = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.doctor_id} {self.date}'


class Appointment(models.Model):
    client_id = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(DoctorProfile, on_delete=models.SET_NULL,null=True)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name="Статус:")

    def __str__(self):
        return f'{self.client_id} {self.date} {self.service_id} ' \
               f'{self.status}'

