from django.db import models


class Email(models.Model):

    email = models.EmailField(null=False, blank=False, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"

    def __str__(self):
        return '%s' % (self.email)
