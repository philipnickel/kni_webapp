from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path("fa-tilbud/", views.contact_view, name="form"),
    path("fa-tilbud/tak/", views.contact_thanks, name="thanks"),
]

