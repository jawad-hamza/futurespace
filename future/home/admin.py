from django.contrib import admin
from .models import Slider, Service, Course, TeamMember, ContactMessage

# Register your models here.
admin.site.register(Slider)
admin.site.register(Service)
admin.site.register(Course)
admin.site.register(TeamMember)
admin.site.register(ContactMessage)