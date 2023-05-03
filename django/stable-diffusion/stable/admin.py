from django.contrib import admin

from stable.models import StableRecord


@admin.register(StableRecord)
class StableRecordAdmin(admin.ModelAdmin):
    pass
