from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.hashers import make_password


class Usuario(DjangoUser):
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return self.username