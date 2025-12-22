from django.contrib import admin
from .models import Activity, ActivityImage

class ActivityImageInline(admin.TabularInline):
    model = ActivityImage
    extra = 1


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "is_featured")  # ✅ FIXED
    list_filter = ("date", "is_featured")
    search_fields = ("title",)
    inlines = [ActivityImageInline]
    list_editable = ("is_featured",)

