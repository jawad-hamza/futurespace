from django.shortcuts import render
from .models import Slider, Service, Course, TeamMember
# Create your views here.


def landing(request):
    sliders = Slider.objects.filter(is_active=True)
    services = Service.objects.all()
    courses = Course.objects.filter(is_active=True)
    team = TeamMember.objects.all()

    context = {
        "sliders": sliders,
        "services": services,
        "courses": courses,
        "team": team,
    }
    return render(request, "home/landing.html", context)
