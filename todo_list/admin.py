from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Task 

admin.site.unregister(User) 

@admin.register(User)
class CustomUserAdmin(ImportExportModelAdmin, UserAdmin):
    pass

@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    list_display = ('title', 'user', 'status', 'due_date', 'is_archived')
    list_filter = ('status', 'is_archived', 'user')
    search_fields = ('title', 'description')