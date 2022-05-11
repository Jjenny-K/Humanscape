from django.contrib import admin
from .models import Study, Institute

admin.site.register([Study, Institute])