from __future__ import unicode_literals
from django.db import models
from django.core.validators import FileExtensionValidator, validate_email

# Create your models here.


class ExcelUpload(models.Model):
    document = models.FileField(upload_to='upload/', validators=[FileExtensionValidator(['xlsx'])])
    upload_at = models.DateTimeField(auto_now_add=True)


class Email(models.Model):
    upload = models.EmailField(max_length=50, blank=False, unique=True, validators=[validate_email])
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.upload
