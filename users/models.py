from django.core.validators import RegexValidator
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^(\+84)?\d{9,15}$')
    phone = models.CharField(validators=[phone_regex], max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
