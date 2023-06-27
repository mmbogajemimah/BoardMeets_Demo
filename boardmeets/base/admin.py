from django.contrib import admin
from .models import Organization, Leader, License

# Register your models here.
admin.site.register(Organization)
admin.site.register(Leader)
admin.site.register(License)