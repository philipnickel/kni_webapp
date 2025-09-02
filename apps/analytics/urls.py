from django.urls import path
from .views import collect

app_name = "analytics"

urlpatterns = [
    path("analytics/collect", collect, name="collect"),
]

