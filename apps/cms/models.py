from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


class CompanyInfo(models.Model):
    """Company information for the tenant"""
    company_name = models.CharField(
        max_length=255,
        verbose_name="Firmanavn",
        help_text="Dit firmas officielle navn"
    )
    tagline = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Slogan",
        help_text="En kort beskrivelse af dit firma (f.eks. 'Kvalitet og håndværk siden 1985')"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Om firmaet",
        help_text="Beskrivelse af din virksomhed, historie og værdier"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Telefon nummer"
    )
    email = models.EmailField(
        blank=True,
        verbose_name="Email adresse"
    )
    address = models.TextField(
        blank=True,
        verbose_name="Adresse",
        help_text="Din virksomheds adresse"
    )
    cvr_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="CVR nummer"
    )
    established_year = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Grundlagt år",
        help_text="Hvilket år blev firmaet grundlagt?"
    )
    
    class Meta:
        verbose_name = "Firma information"
        verbose_name_plural = "Firma information"
    
    def __str__(self):
        return self.company_name or "Firma information"


class Service(models.Model):
    """Services offered by the construction business"""
    name = models.CharField(
        max_length=200,
        verbose_name="Service navn",
        help_text="F.eks. 'Køkken renovering', 'Træ terrasser', 'Tømrer arbejde'"
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        verbose_name="URL slug"
    )
    description = models.TextField(
        verbose_name="Beskrivelse",
        help_text="Detaljeret beskrivelse af servicen"
    )
    short_description = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Kort beskrivelse",
        help_text="Kort beskrivelse til service oversigt"
    )
    icon_class = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Ikon klasse",
        help_text="CSS ikon klasse (f.eks. 'fas fa-hammer')"
    )
    featured = models.BooleanField(
        default=False,
        verbose_name="Fremhævet service",
        help_text="Vis denne service fremhævet på forsiden"
    )
    active = models.BooleanField(
        default=True,
        verbose_name="Aktiv",
        help_text="Er denne service aktiv og tilgængelig?"
    )
    order = models.IntegerField(
        default=0,
        verbose_name="Rækkefølge",
        help_text="Rækkefølge services vises i (lavere tal = højere prioritet)"
    )
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Service"
        verbose_name_plural = "Services"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Project(models.Model):
    """Construction projects for portfolio"""
    title = models.CharField(
        max_length=255,
        verbose_name="Projekt titel",
        help_text="F.eks. 'Køkken renovering' eller 'Træ terrasse'"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        verbose_name="URL slug"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Projekt beskrivelse",
        help_text="Beskriv arbejdet, materialer og proces"
    )
    project_type = models.CharField(
        max_length=100,
        choices=[
            ('renovation', 'Renovering'),
            ('nybyggeri', 'Nybyggeri'),
            ('tilbygning', 'Tilbygning'),
            ('reparation', 'Reparation'),
            ('haandvaerk', 'Håndværk'),
            ('andet', 'Andet'),
        ],
        default='haandvaerk',
        verbose_name="Projekt type"
    )
    materials = models.TextField(
        blank=True,
        verbose_name="Materialer brugt",
        help_text="F.eks. 'Jatoba træ', 'Lærk', 'Eg', osv."
    )
    client_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Kunde navn",
        help_text="Valgfrit - kunde navn (anonymt eller med tilladelse)"
    )
    location = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Lokation",
        help_text="F.eks. 'København', 'Privat bolig', eller 'Erhverv'"
    )
    featured = models.BooleanField(
        default=False,
        verbose_name="Featured projekt",
        help_text="Vis dette projekt fremhævet på forsiden"
    )
    published = models.BooleanField(
        default=True,
        verbose_name="Synlig på hjemmeside",
        help_text="Skal projektet vises på hjemmesiden?"
    )
    completion_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Færdiggørelse dato",
        help_text="Hvornår blev projektet færdiggjort?"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Oprettet"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Opdateret"
    )
    
    class Meta:
        ordering = ['-completion_date', '-created_at']
        verbose_name = "Projekt"
        verbose_name_plural = "Projekter"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_first_image(self):
        """Get the first image for thumbnails"""
        return self.images.first()
    
    def get_absolute_url(self):
        return f'/projekter/{self.slug}/'


class ProjectImage(models.Model):
    """Images for construction projects"""
    project = models.ForeignKey(
        Project,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Projekt"
    )
    image = models.ImageField(
        upload_to='projects/%Y/%m/',
        verbose_name="Billede"
    )
    caption = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Billedtekst",
        help_text="Valgfri beskrivelse af billedet"
    )
    alt_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Alt tekst",
        help_text="Beskrivelse for skærmlæsere"
    )
    order = models.IntegerField(
        default=0,
        verbose_name="Rækkefølge",
        help_text="Rækkefølge billederne vises i"
    )
    
    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Projekt billede"
        verbose_name_plural = "Projekt billeder"
    
    def __str__(self):
        return f"{self.project.title} - Billede {self.order + 1}"


class Testimonial(models.Model):
    """Client testimonials and reviews"""
    name = models.CharField(
        max_length=200,
        verbose_name="Kunde navn",
        help_text="Kundens navn (eller anonymt som 'Privat kunde')"
    )
    title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Kunde titel/rolle",
        help_text="F.eks. 'Boligejer', 'Ejendomsudvikler', etc."
    )
    content = models.TextField(
        verbose_name="Testimonial",
        help_text="Kundens udtalelse om jeres arbejde"
    )
    project_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Relateret projekt",
        help_text="Hvilket projekt drejer testimonial'en sig om?"
    )
    rating = models.IntegerField(
        choices=[(i, f"{i} stjerner") for i in range(1, 6)],
        default=5,
        verbose_name="Vurdering",
        help_text="Antal stjerner (1-5)"
    )
    featured = models.BooleanField(
        default=False,
        verbose_name="Fremhævet testimonial",
        help_text="Vis denne testimonial fremhævet på forsiden"
    )
    active = models.BooleanField(
        default=True,
        verbose_name="Aktiv",
        help_text="Skal denne testimonial vises på hjemmesiden?"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Oprettet"
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Kundeanmeldelse"
        verbose_name_plural = "Kundeanmeldelser"
    
    def __str__(self):
        return f"{self.name} - {self.rating} stjerner"


class ContactSubmission(models.Model):
    """Contact form submissions from the website"""
    name = models.CharField(
        max_length=200,
        verbose_name="Navn"
    )
    email = models.EmailField(
        verbose_name="Email"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Telefon"
    )
    subject = models.CharField(
        max_length=300,
        verbose_name="Emne"
    )
    message = models.TextField(
        verbose_name="Besked"
    )
    project_type = models.CharField(
        max_length=100,
        choices=[
            ('renovation', 'Renovering'),
            ('nybyggeri', 'Nybyggeri'),
            ('tilbygning', 'Tilbygning'),
            ('reparation', 'Reparation'),
            ('haandvaerk', 'Håndværk'),
            ('tilbud', 'Forespørgsel på tilbud'),
            ('andet', 'Andet'),
        ],
        blank=True,
        verbose_name="Projekt type"
    )
    budget_range = models.CharField(
        max_length=100,
        choices=[
            ('under_50k', 'Under 50.000 kr'),
            ('50k_100k', '50.000 - 100.000 kr'),
            ('100k_250k', '100.000 - 250.000 kr'),
            ('250k_500k', '250.000 - 500.000 kr'),
            ('over_500k', 'Over 500.000 kr'),
            ('flexible', 'Fleksibel'),
        ],
        blank=True,
        verbose_name="Budget interval"
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name="Læst"
    )
    is_replied = models.BooleanField(
        default=False,
        verbose_name="Besvaret"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Modtaget"
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Henvendelse"
        verbose_name_plural = "Henvendelser"
    
    def __str__(self):
        return f"{self.name} - {self.subject}"