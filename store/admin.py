from django.contrib import admin
from . import models

#register models
admin.site.register(models.Collection)
admin.site.register(models.Product)