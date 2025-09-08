from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from django.forms import TextInput, Textarea
from .models import CompanyInfo, Service, Project, ProjectImage, Testimonial, ContactSubmission


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    max_num = 10
    fields = ('image', 'caption', 'alt_text', 'order')
    ordering = ['order']


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Grundlæggende information', {
            'fields': ('company_name', 'tagline', 'description')
        }),
        ('Kontakt information', {
            'fields': ('phone', 'email', 'address')
        }),
        ('Virksomhedsdata', {
            'fields': ('cvr_number', 'established_year')
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one CompanyInfo instance
        if CompanyInfo.objects.exists():
            return False
        return super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion of company info
        return False


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_preview', 'featured', 'active', 'order')
    list_filter = ('featured', 'active')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('featured', 'active', 'order')
    ordering = ['order', 'name']
    
    fieldsets = (
        ('Grundlæggende information', {
            'fields': ('name', 'slug', 'short_description')
        }),
        ('Detaljeret beskrivelse', {
            'fields': ('description', 'icon_class')
        }),
        ('Indstillinger', {
            'fields': ('featured', 'active', 'order')
        }),
    )
    
    def service_preview(self, obj):
        """Show service preview"""
        icon = f'<i class="{obj.icon_class}" style="color: #4d7a3a; margin-right: 5px;"></i>' if obj.icon_class else ''
        preview = obj.short_description or obj.description
        if len(preview) > 60:
            preview = preview[:60] + '...'
        return format_html(f'{icon}{preview}')
    service_preview.short_description = 'Preview'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_thumbnail', 'project_type', 'completion_date', 'featured', 'published')
    list_filter = ('project_type', 'featured', 'published', 'completion_date')
    search_fields = ('title', 'description', 'client_name', 'location')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('featured', 'published')
    date_hierarchy = 'completion_date'
    ordering = ['-completion_date', '-created_at']
    
    inlines = [ProjectImageInline]
    
    fieldsets = (
        ('Grundlæggende information', {
            'fields': ('title', 'slug', 'published', 'featured')
        }),
        ('Projekt detaljer', {
            'fields': ('description', 'project_type', 'materials', 'completion_date')
        }),
        ('Kunde information', {
            'fields': ('client_name', 'location'),
            'classes': ('collapse',)
        }),
    )
    
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 60})},
    }
    
    def project_thumbnail(self, obj):
        """Display project thumbnail"""
        first_image = obj.get_first_image()
        if first_image and first_image.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 4px;" />',
                first_image.image.url
            )
        return format_html(
            '<div style="width: 60px; height: 60px; background: #f5f5f5; border-radius: 4px; '
            'display: flex; align-items: center; justify-content: center; color: #999; font-size: 12px;">'
            'Ingen billede</div>'
        )
    project_thumbnail.short_description = 'Billede'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars_display', 'project_title', 'featured', 'active', 'created_at')
    list_filter = ('rating', 'featured', 'active', 'created_at')
    search_fields = ('name', 'content', 'project_title')
    list_editable = ('featured', 'active')
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Kunde information', {
            'fields': ('name', 'title', 'project_title')
        }),
        ('Anmeldelse', {
            'fields': ('content', 'rating')
        }),
        ('Indstillinger', {
            'fields': ('featured', 'active')
        }),
    )
    
    def stars_display(self, obj):
        """Display star rating visually"""
        stars = '★' * obj.rating + '☆' * (5 - obj.rating)
        return format_html(
            '<span style="color: #ffd700; font-size: 16px;" title="{} stjerner">{}</span>',
            obj.rating,
            stars
        )
    stars_display.short_description = 'Vurdering'


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'project_type', 'budget_range', 'is_read', 'is_replied', 'status_display', 'created_at')
    list_filter = ('is_read', 'is_replied', 'project_type', 'budget_range', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'project_type', 'budget_range', 'created_at')
    list_editable = ('is_read', 'is_replied')
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Kunde information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Henvendelse', {
            'fields': ('subject', 'message', 'project_type', 'budget_range')
        }),
        ('Status', {
            'fields': ('is_read', 'is_replied')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def status_display(self, obj):
        """Display status with colors"""
        if obj.is_replied:
            return format_html('<span style="color: #28a745;">✓ Besvaret</span>')
        elif obj.is_read:
            return format_html('<span style="color: #ffc107;">👁 Læst</span>')
        else:
            return format_html('<span style="color: #dc3545; font-weight: bold;">● Ny</span>')
    status_display.short_description = 'Status'
    
    def has_add_permission(self, request):
        # Contact submissions are created via the website form, not admin
        return False


# Custom admin site styling
admin.site.site_header = "Indhold Administration"
admin.site.site_title = "CMS Admin"
admin.site.index_title = "Velkommen til din hjemmeside administration"