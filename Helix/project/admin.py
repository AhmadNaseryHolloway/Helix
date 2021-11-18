from django.contrib import admin

from .models import Project, Tasks, Project_Milestones, Stage_Payment, Stage_Payment_Description, Stage, TaskType, ResourceNames, ProjectTasks
# Register your models here.

admin.site.register(Project)
admin.site.register(Tasks)
admin.site.register(Project_Milestones)
admin.site.register(Stage_Payment_Description)
admin.site.register(Stage_Payment)
admin.site.register(Stage)
admin.site.register(TaskType)
admin.site.register(ResourceNames)
admin.site.register(ProjectTasks)
