from django.contrib import admin
from django.urls import include, path
from home.views import contact_submit, landing
app_name = "home"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path("contact/submit/", contact_submit, name="contact_submit"),
]
