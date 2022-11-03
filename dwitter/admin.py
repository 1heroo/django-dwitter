from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Profile, Dweet


class ItemInline(admin.StackedInline):
    model = Profile
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    model = User
    # Only display the "username" field
    fields = ["username"]

admin.site.register(Dweet)
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
