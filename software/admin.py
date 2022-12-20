from django.contrib import admin
from software.models import Software


# Register your models here.
class SoftwareAdmin(admin.ModelAdmin):
    pass
admin.site.register(Software, SoftwareAdmin)