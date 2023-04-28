from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin de usuarios"""

    list_display = (
        'id',
        'username',
        'is_approved',
    )
