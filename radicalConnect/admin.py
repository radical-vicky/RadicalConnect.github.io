from django.contrib import admin
from django.contrib.auth.base_user import BaseUserManager

from radicalConnect.models import Contact, FutureSkill

# Register your models here.
admin.site.register(Contact)
admin.site.register(FutureSkill)




