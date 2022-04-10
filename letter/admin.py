from django.contrib import admin

# Register your models here.
from . models import MailMessage, Subscribers

# Register your models here.
admin.site.register(MailMessage)
admin.site.register(Subscribers)
