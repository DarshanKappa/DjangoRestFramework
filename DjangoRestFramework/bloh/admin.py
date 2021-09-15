from django.contrib import admin
from django.db import models
from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.Category)
admin.site.register(models.Post)
