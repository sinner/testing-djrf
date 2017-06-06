from django.db import models
from django.conf import settings
from .TimeStampable import TimeStampable


class Contact(TimeStampable):

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=15, blank=True, null=True)

    def create_user(self, email, password):
        self.user.set_email(email)
        self.user.set_password(password)

    def __str__(self):
        return self.name
