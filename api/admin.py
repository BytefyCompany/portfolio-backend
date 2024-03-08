from django.contrib import admin
from . import models


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "picture", "id")

class AboutAdmin(admin.ModelAdmin):
    list_display = ("text", "updated_at", "id")

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("full_name", "working_experience","id")

class PAdmin(admin.ModelAdmin):
    list_display = ("name", "id")

class ContactAdmin(admin.ModelAdmin):
    list_display = ("full_name", "message", "id")


admin.site.register(models.TeamMember, TeamMemberAdmin)
admin.site.register(models.About, AboutAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ProgrammingLang, PAdmin)
admin.site.register(models.Contact, ContactAdmin)
