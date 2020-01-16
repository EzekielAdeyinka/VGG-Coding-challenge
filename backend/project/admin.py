
# project/admin.py
    
from django.contrib import admin
from .models import Project # add this
    
class ProjectAdmin(admin.ModelAdmin):  # add this
  list_display = ('name', 'description', 'completed') # add this
        
# Register your models here.
admin.site.register(Project, ProjectAdmin) # add this
