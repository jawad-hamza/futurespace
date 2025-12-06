from django.shortcuts import render
from .models import Slider, Service, Course, TeamMember , PromoCard 
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
        "club_card": PromoCard.objects.get(key="club"),
        "activity_card": PromoCard.objects.get(key="activity"),
  
    }
    return render(request, "home/landing.html", context)
