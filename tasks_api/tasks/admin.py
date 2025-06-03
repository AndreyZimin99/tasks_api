from django.contrib import admin

from .models import (
    Board,
    Column,
    Group,
    Sprint,
    Task,
)

admin.site.register(Task)
admin.site.register(Board)
admin.site.register(Sprint)
admin.site.register(Column)
admin.site.register(Group)
