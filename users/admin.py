from django.contrib import admin

from users.models import SWOUser


class SWOUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(SWOUser, SWOUserAdmin)
