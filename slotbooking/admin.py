from django.contrib import admin
from django.contrib.auth.models import User
from .models import Database, Player
# Register your models here.

admin.site.register(Database)
admin.site.register(Player)