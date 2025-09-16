from django.db import models


class ContactSubmission(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In progress"),
        ("closed", "Closed"),
    ]

    site = models.ForeignKey("wagtailcore.Site", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=64, blank=True)
    message = models.TextField(blank=True)
    consent = models.BooleanField(default=False)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="new")

    def __str__(self):
        return f"{self.name} — {self.created_at:%Y-%m-%d}"

