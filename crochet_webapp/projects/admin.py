from django.contrib import admin
from projects.models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'completed']

class ProjectSectionAdmin(admin.ModelAdmin):
    list_display = ['get_project_name', 'section_name', 'row_count']

    def get_project_name(self, obj):
        return obj.project.name
    
class YarnAdmin(admin.ModelAdmin):
    list_display = ['brand', 'name', 'type', 'weight']

class YarnColourAdmin(admin.ModelAdmin):
    list_display = ['get_yarn_details', 'colour_id', 'colour_name', 'num_skeins']

    def get_yarn_details(self, obj):
        yarn = obj.project.yarn
        return '%s %s %s' % (yarn.brand, yarn.name, yarn.weight)
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectSection, ProjectSectionAdmin)
admin.site.register(Yarn, YarnAdmin)
admin.site.register(YarnColour, YarnColourAdmin)
