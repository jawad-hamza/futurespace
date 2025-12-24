from django.db import models

# Create your models here.
from django.db import models

# 1️⃣ Slider
class Slider(models.Model):
    title = models.CharField(max_length=150, blank=True)
    subtitle = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to="slider/")
    button_text = models.CharField(max_length=50, blank=True)
    button_link = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or "Slider Image"


# 2️⃣ Services
class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="services/")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


# 3️⃣ Courses
class Course(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="courses/")
    is_active = models.BooleanField(default=True)
    buy_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


# 4️⃣ Team Members
class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="team/")
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


# 5️⃣ Contact Form
class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    is_read = models.BooleanField(default=False)  # 👈 NEW

    def __str__(self):
        return f"Message from {self.name}"



# 6️⃣ Activities moved to activity app, not here

class PromoCard(models.Model):
    TITLE_CHOICES = (
        ("club", "Club"),
        ("activity", "Activity"),
    )
    key = models.CharField(
        max_length=20,
        choices=TITLE_CHOICES,
        unique=True,
        help_text="Unique slug: club or activity"
    )
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="promo_cards/")
    link = models.URLField(blank=True, help_text="Full URL or relative path to page")

    def __str__(self):
        return f"{self.get_key_display()} card"

    class Meta:
        verbose_name = "Promo Card"
        verbose_name_plural = "Promo Cards"