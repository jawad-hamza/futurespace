from django.contrib import admin
from .models import PromoCard, Slider, Service, Course, TeamMember, ContactMessage
from django.utils.html import format_html
from django.utils import timezone
from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home"

    def ready(self):
        import home.signals

# Register your models here.
admin.site.register(Slider)
admin.site.register(Service)
admin.site.register(PromoCard)
admin.site.register(Course)
admin.site.register(TeamMember)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("status_dot", "name", "email_link", "short_message", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "message")
    ordering = ("-created_at",)
    list_per_page = 25

    readonly_fields = (
        "name",
        "email",
        "message",
        "created_at",
        "reply_button",
    )

    actions = ["mark_as_read"]

    def status_dot(self, obj):
        return format_html(
            '<span style="color:{};font-weight:bold;">●</span>',
            "#dc2626" if not obj.is_read else "#16a34a",
        )

    status_dot.short_description = ""

    def short_message(self, obj):
        preview = obj.message[:70] + "..." if len(obj.message) > 70 else obj.message
        return format_html("<strong>{}</strong>", preview) if not obj.is_read else preview

    short_message.short_description = "Message"

    def email_link(self, obj):
        return format_html(
            '<a href="mailto:{}">{}</a>',
            obj.email,
            obj.email,
        )

    email_link.short_description = "Email"

    def reply_button(self, obj):
        gmail_url = (
            "https://mail.google.com/mail/?view=cm"
            f"&to={obj.email}"
            "&su=Re:%20Your%20message%20to%20FutureSpace"
        )

        return format_html(
            '<a class="button" href="{}">Mail Client</a>&nbsp;'
            '<a class="button" href="{}" target="_blank" '
            'style="background:#ea4335;color:white;">Gmail</a>',
            f"mailto:{obj.email}",
            gmail_url,
        )

    def change_view(self, request, object_id, form_url="", extra_context=None):
        obj = self.get_object(request, object_id)
        if obj and not obj.is_read:
            obj.is_read = True
            obj.save(update_fields=["is_read"])
        return super().change_view(request, object_id, form_url, extra_context)

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    mark_as_read.short_description = "Mark selected messages as read"