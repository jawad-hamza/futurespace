from django.contrib import admin
from django.utils import timezone
from .models import ContactMessage

def dashboard_message_stats(request):
    today = timezone.now().date()

    return {
        "new_messages_today": ContactMessage.objects.filter(
            created_at__date=today
        ).count(),
        "unread_messages": ContactMessage.objects.filter(is_read=False).count(),
    }

admin.site.each_context = lambda request: {
    **admin.site.each_context(request),
    **dashboard_message_stats(request),
}
