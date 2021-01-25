from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class MyUserManager(BaseUserManager):
    def create_user(self, CargoFuncionario, email, name, password=None):
        if not email:
            raise ValueError("Usuários precisam ter um email")
        if not name:
            raise ValueError("Usuários precisam ter um nome")
        if not CargoFuncionario:
            raise ValueError("Usuários precisam ter um cargo")

        user = self.model(
            CargoFuncionario=CargoFuncionario,
            email=self.normalize_email(email),
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        cargo = CargoFuncionario.objects.get(cd_CargoFuncionario=1)
        user = self.create_user(
            CargoFuncionario=cargo,
            email=self.normalize_email(email),
            password=password,
            name=name,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CargoFuncionario(models.Model):
    cd_CargoFuncionario = models.AutoField(primary_key=True, null=False)
    ds_CargoFuncionario = models.CharField(max_length=45, null=False)


class User(AbstractUser):
    CargoFuncionario = models.ForeignKey(CargoFuncionario, null=False, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True, verbose_name="email")
    date_joined = models.DateTimeField(verbose_name="data_joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    object = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)