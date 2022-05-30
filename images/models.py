from django.db import models
from django.conf import settings


class Image(models.Model):
    label = models.CharField('Label', max_length=255)
    url = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label

# Create your models here.
