from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from wagtail.models import Site
import logging

from .forms import ContactForm
from .models import ContactSubmission

logger = logging.getLogger(__name__)


def _site(request: HttpRequest) -> Site:
    return Site.find_for_request(request)


def send_contact_emails(contact_submission: ContactSubmission, request: HttpRequest) -> None:
    """Send email notifications for new contact form submissions."""
    try:
        site = contact_submission.site

        # Email to admin/company
        admin_subject = f"Ny henvendelse fra {contact_submission.name}"
        admin_message = f"""
Ny kontaktformular indsendelse:

Navn: {contact_submission.name}
Email: {contact_submission.email}
Telefon: {contact_submission.phone or 'Ikke angivet'}
Besked: {contact_submission.message or 'Ingen besked'}

Indtastet: {contact_submission.created_at.strftime('%d/%m/%Y %H:%M')}

Login til admin for at se flere detaljer: {settings.WAGTAILADMIN_BASE_URL}/admin/
        """.strip()

        # Send to admin email
        admin_email = getattr(settings, 'ADMIN_EMAIL', getattr(settings, 'DEFAULT_FROM_EMAIL', 'admin@example.com'))

        send_mail(
            subject=admin_subject,
            message=admin_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[admin_email],
            fail_silently=False,
        )

        # Confirmation email to customer
        customer_subject = "Tak for din henvendelse - JCleemannByg"
        customer_message = f"""
Hej {contact_submission.name},

Tak for din henvendelse til JCleemannByg!

Vi har modtaget din besked og vil kontakte dig inden for 24 timer på hverdage.

Dit indsendte besked:
{contact_submission.message or 'Ingen specifik besked angivet'}

Hvis du har akutte spørgsmål, er du velkommen til at ringe direkte på +45 12 34 56 78.

Med venlig hilsen
JCleemannByg Team

---
Åbningstider:
Man-Fre: 07:00-17:00
Lør: 08:00-14:00
Søn: Kun akutte sager
        """.strip()

        send_mail(
            subject=customer_subject,
            message=customer_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[contact_submission.email],
            fail_silently=False,
        )

        logger.info(f"Contact form emails sent successfully for submission {contact_submission.id}")

    except Exception as e:
        logger.error(f"Failed to send contact form emails for submission {contact_submission.id}: {e}")
        # Don't raise the exception to avoid breaking the form submission flow


@csrf_exempt
def contact_view(request: HttpRequest) -> HttpResponse:
    site = _site(request)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            instance: ContactSubmission = form.save(commit=False)
            instance.site = site
            instance.save()

            # Send email notifications
            try:
                send_contact_emails(instance, request)
                messages.success(request, 'Din besked er blevet sendt. Du vil modtage en bekræftelsesmail snarest.')
            except Exception as e:
                logger.error(f"Email sending failed: {e}")
                messages.warning(request, 'Din besked er blevet sendt, men der opstod et problem med bekræftelses-emailen.')

            return redirect("contacts:thanks")
    else:
        form = ContactForm()
    return render(request, "contacts/form.html", {"form": form})


def contact_thanks(request: HttpRequest) -> HttpResponse:
    return render(request, "contacts/thanks.html")


def send_quote_request_emails(data: dict, request: HttpRequest) -> None:
    """Send email notifications for new quote request submissions."""
    try:
        # Email to admin/company
        admin_subject = f"Ny tilbudsanmodning fra {data['name']}"
        admin_message = f"""
Ny tilbudsanmodning indsendelse:

Navn: {data['name']}
Email: {data['email']}
Telefon: {data['phone']}
Lokation: {data.get('location', 'Ikke angivet')}
Projekt type: {data.get('project_type', 'Ikke angivet')}
Budget: {data.get('budget_range', 'Ikke angivet')}
Tidsramme: {data.get('timeline', 'Ikke angivet')}

Projekt beskrivelse:
{data.get('description', 'Ingen beskrivelse')}

Login til admin for at se flere detaljer: {settings.WAGTAILADMIN_BASE_URL}/admin/
        """.strip()

        # Send to admin email
        admin_email = getattr(settings, 'ADMIN_EMAIL', getattr(settings, 'DEFAULT_FROM_EMAIL', 'admin@example.com'))

        send_mail(
            subject=admin_subject,
            message=admin_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[admin_email],
            fail_silently=False,
        )

        # Confirmation email to customer
        customer_subject = "Tak for din tilbudsanmodning - JCleemannByg"
        customer_message = f"""
Hej {data['name']},

Tak for din tilbudsanmodning til JCleemannByg!

Vi har modtaget din anmodning og vil kontakte dig med et skræddersyet tilbud inden for 24 timer på hverdage.

Dit projekt:
- Type: {data.get('project_type', 'Ikke angivet')}
- Lokation: {data.get('location', 'Ikke angivet')}
- Budget: {data.get('budget_range', 'Ikke angivet')}
- Tidsramme: {data.get('timeline', 'Ikke angivet')}

Beskrivelse:
{data.get('description', 'Ingen beskrivelse')}

Hvis du har akutte spørgsmål, er du velkommen til at ringe direkte på +45 12 34 56 78.

Med venlig hilsen
JCleemannByg Team

---
Åbningstider:
Man-Fre: 07:00-17:00
Lør: 08:00-14:00
Søn: Kun akutte sager
        """.strip()

        send_mail(
            subject=customer_subject,
            message=customer_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[data['email']],
            fail_silently=False,
        )

        logger.info(f"Quote request emails sent successfully for {data['email']}")

    except Exception as e:
        logger.error(f"Failed to send quote request emails for {data['email']}: {e}")
        # Don't raise the exception to avoid breaking the form submission flow


@csrf_exempt
def quote_request_view(request: HttpRequest) -> HttpResponse:
    """Handle quote request form submissions."""
    if request.method == "POST":
        # Extract form data
        data = {
            'name': request.POST.get('name', '').strip(),
            'email': request.POST.get('email', '').strip(),
            'phone': request.POST.get('phone', '').strip(),
            'location': request.POST.get('location', '').strip(),
            'project_type': request.POST.get('project_type', '').strip(),
            'budget_range': request.POST.get('budget_range', '').strip(),
            'timeline': request.POST.get('timeline', '').strip(),
            'description': request.POST.get('description', '').strip(),
            'privacy_consent': request.POST.get('privacy_consent', '') == 'on',
        }

        # Basic validation
        if not all([data['name'], data['email'], data['phone'], data['description']]):
            messages.error(request, 'Udfyld venligst alle obligatoriske felter.')
            return redirect(request.META.get('HTTP_REFERER', '/'))

        if not data['privacy_consent']:
            messages.error(request, 'Du skal acceptere behandling af personoplysninger for at fortsætte.')
            return redirect(request.META.get('HTTP_REFERER', '/'))

        # Send email notifications
        try:
            send_quote_request_emails(data, request)
            messages.success(request, 'Din tilbudsanmodning er blevet sendt. Vi kontakter dig inden for 24 timer.')
        except Exception as e:
            logger.error(f"Quote request email sending failed: {e}")
            messages.warning(request, 'Din anmodning er modtaget, men der opstod et problem med bekræftelses-emailen.')

        return redirect("contacts:quote_request_thanks")

    # If GET request, redirect to homepage
    return redirect('/')


def quote_request_thanks(request: HttpRequest) -> HttpResponse:
    """Thank you page for quote requests."""
    return render(request, "contacts/quote_thanks.html")

