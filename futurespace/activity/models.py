from django.db import models
from PIL import Image

class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class ActivityImage(models.Model):
    activity = models.ForeignKey(
        Activity,
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="activities/")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img_path = self.image.path
        img = Image.open(img_path)

        # Convert to RGB (important for PNGs)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # Resize if too large
        max_width = 1600
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.LANCZOS)

        # Compress & save
        img.save(img_path, optimize=True, quality=80)

    def __str__(self):
        return f"Image for {self.activity.title}"