from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import StudentsDb, FocusUser

class FocusUserAdmin(UserAdmin):
    model = FocusUser
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("focus_req",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("focus_req",)}),)

# Register your models here.
admin.site.register(StudentsDb)
admin.site.register(FocusUser, FocusUserAdmin)