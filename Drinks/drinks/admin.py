# This file help display your database table in your admin page
from django.contrib import admin
from .models import Drinks

admin.site.register(Drinks)