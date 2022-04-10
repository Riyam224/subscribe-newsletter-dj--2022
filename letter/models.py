from django.db import models
from django.utils.translation import gettext_lazy as _



class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = _("Subscribe")
        verbose_name_plural = _("Subscribes")

        
    def __str__(self):
        return self.email

 
class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title