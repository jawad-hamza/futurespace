from django.contrib import messages
from django.views.decorators.http import require_POST

from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import ContactMessage, Slider, Service, Course, TeamMember , PromoCard 
from .forms import ContactForm
# Create your views here.


def landing(request):
    sliders = Slider.objects.filter(is_active=True)
    services = Service.objects.all()
    courses = Course.objects.filter(is_active=True)
    team = TeamMember.objects.all()
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # get cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # You can either save to DB or send email — we’ll do an email by default
            # (configure email settings later)

            # send email logic here (optional)
            from django.core.mail import send_mail
            send_mail(
                subject=f"New Contact Us Message from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=email,                # from visitor
                recipient_list=["info@futurespaceuk.com"],  # your address
                fail_silently=False,
            )

            messages.success(request, "Your message was sent successfully!")
            return redirect('landing')  # or redirect back to same page

    context = {
        "sliders": sliders,
        "services": services,
        "courses": courses,
        "team": team,
        "club_card": PromoCard.objects.get(key="club"),
        "activity_card": PromoCard.objects.get(key="activity"),
        "contact_form": form,
  
    }
    return render(request, "home/landing.html", context)

@require_POST
def contact_submit(request):
    try:
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not name or not email or not message:
            return JsonResponse({
                "status": "error",
                "message": "All fields are required."
            })

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return JsonResponse({
            "status": "success",
            "message": "Message sent successfully!"
        })

    except Exception:
        return JsonResponse({
            "status": "error",
            "message": "Something went wrong. Please try again."
        })