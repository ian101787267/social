from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Post, Comment, FriendRequest

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'friends')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FriendRequest)




