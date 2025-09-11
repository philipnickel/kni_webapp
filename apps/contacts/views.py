from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse
from wagtail.models import Site

from .forms import ContactForm
from .models import ContactSubmission


def _site(request: HttpRequest) -> Site:
    return Site.find_for_request(request)


@csrf_exempt
def contact_view(request: HttpRequest) -> HttpResponse:
    site = _site(request)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            instance: ContactSubmission = form.save(commit=False)
            instance.site = site
            instance.save()
            return redirect("contacts:thanks")
    else:
        form = ContactForm()
    return render(request, "contacts/form.html", {"form": form})


def contact_thanks(request: HttpRequest) -> HttpResponse:
    return render(request, "contacts/thanks.html")

