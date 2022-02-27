import django
from django.contrib import admin
import django.apps
# Register your models here.
models = django.apps.apps.get_models()

for model in models:
  try:
    admin.site.register(model)
  except admin.sites.AlreadyRegistered:
    pass
    

