from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, name,  email, password, **extra_fields):
        user = self.model(name=name, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.full_clean()
        user.save()
        return user

    def create_user(self, name,  email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name,  email, password, **extra_fields)

    def create_superuser(self, name,  email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have staff priviledges')
        return self._create_user(name,  email, password, **extra_fields)
