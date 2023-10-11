from django.contrib import admin
from . import models
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')

admin.site.register(models.Project,ProjectAdmin)