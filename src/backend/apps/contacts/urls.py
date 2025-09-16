from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path("fa-tilbud/", views.contact_view, name="form"),
    path("fa-tilbud/tak/", views.contact_thanks, name="thanks"),
    path("quote-request/", views.quote_request_view, name="quote_request"),
    path("quote-request/tak/", views.quote_request_thanks, name="quote_request_thanks"),
]

