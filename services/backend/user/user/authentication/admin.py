from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

admin.site.register(User, UserAdmin)

# Register your models here.
