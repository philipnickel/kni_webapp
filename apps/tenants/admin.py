from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django_tenants.admin import TenantAdminMixin
from django_tenants.utils import schema_context
from .models import Client, Domain, Theme


class DomainInline(admin.TabularInline):
    model = Domain
    extra = 1


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'schema_name', 'primary_domain', 'theme_preview', 'is_active', 'created_on')
    list_filter = ('is_active', 'theme', 'created_on')
    search_fields = ('name', 'schema_name', 'contact_email', 'description')
    readonly_fields = ('schema_name', 'created_on', 'updated_on', 'theme_colors_preview')
    actions = ['create_tenant_schemas', 'activate_tenants', 'deactivate_tenants']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'schema_name')
        }),
        ('Contact Details', {
            'fields': ('contact_email', 'phone_number', 'address', 'cvr_number')
        }),
        ('Branding', {
            'fields': ('theme', 'theme_colors_preview')
        }),
        ('System', {
            'fields': ('is_active', 'created_on', 'updated_on'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [DomainInline]
    
    def primary_domain(self, obj):
        domain = obj.primary_domain
        return domain.domain if domain else "No domain"
    primary_domain.short_description = "Primary Domain"
    
    def theme_preview(self, obj):
        if obj.theme:
            return format_html(
                '<div style="display: inline-flex; align-items: center;">'
                '<div style="width: 20px; height: 20px; background-color: {}; border: 1px solid #ccc; margin-right: 8px;"></div>'
                '{}</div>',
                obj.theme.primary_color,
                obj.theme.name
            )
        return "No theme"
    theme_preview.short_description = "Theme"
    
    def theme_colors_preview(self, obj):
        if not obj.theme:
            return "No theme selected"
        
        colors = [
            ('Primary', obj.theme.primary_color),
            ('Primary Hover', obj.theme.primary_hover_color),
            ('Hero Start', obj.theme.hero_start_color),
            ('Hero End', obj.theme.hero_end_color),
            ('Footer BG', obj.theme.footer_bg_color),
            ('Footer Text', obj.theme.footer_text_color),
        ]
        
        preview_html = '<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; padding: 10px;">'
        for name, color in colors:
            preview_html += f'''
                <div style="display: flex; align-items: center; gap: 8px;">
                    <div style="width: 30px; height: 30px; background-color: {color}; border: 1px solid #ccc; border-radius: 4px;"></div>
                    <div>
                        <strong>{name}</strong><br/>
                        <code style="font-size: 11px;">{color}</code>
                    </div>
                </div>
            '''
        preview_html += '</div>'
        return mark_safe(preview_html)
    theme_colors_preview.short_description = "Theme Colors"
    
    def create_tenant_schemas(self, request, queryset):
        created_count = 0
        for client in queryset:
            try:
                # Check if schema already exists
                with schema_context(client.schema_name):
                    created_count += 1
            except Exception as e:
                # Schema doesn't exist, try to create it
                try:
                    client.create_schema()
                    created_count += 1
                except Exception as create_error:
                    self.message_user(
                        request,
                        f"Failed to create schema for {client.name}: {create_error}",
                        level='ERROR'
                    )
        
        if created_count:
            self.message_user(
                request,
                f"Successfully ensured {created_count} tenant schema(s) exist."
            )
    create_tenant_schemas.short_description = "Create tenant schemas"
    
    def activate_tenants(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f"Activated {updated} tenant(s).")
    activate_tenants.short_description = "Activate selected tenants"
    
    def deactivate_tenants(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f"Deactivated {updated} tenant(s).")
    deactivate_tenants.short_description = "Deactivate selected tenants"


@admin.register(Domain)  
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')
    list_filter = ('is_primary',)
    search_fields = ('domain', 'tenant__name')
    raw_id_fields = ('tenant',)


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'primary_color_preview', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'slug', 'description')
    readonly_fields = ('created_at', 'updated_at', 'color_preview')
    prepopulated_fields = {'slug': ('name',)}
    actions = ['activate_themes', 'deactivate_themes']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description', 'is_active')
        }),
        ('Primary Colors', {
            'fields': ('primary_color', 'primary_hover_color')
        }),
        ('Hero Section Colors', {
            'fields': ('hero_start_color', 'hero_end_color')
        }),
        ('Footer Colors', {
            'fields': ('footer_bg_color', 'footer_text_color')
        }),
        ('Preview', {
            'fields': ('color_preview',),
            'classes': ('wide',)
        }),
        ('System', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def primary_color_preview(self, obj):
        return format_html(
            '<div style="display: inline-flex; align-items: center;">'
            '<div style="width: 20px; height: 20px; background-color: {}; border: 1px solid #ccc; margin-right: 8px; border-radius: 3px;"></div>'
            '{}</div>',
            obj.primary_color,
            obj.primary_color
        )
    primary_color_preview.short_description = "Primary Color"
    
    def color_preview(self, obj):
        preview_html = '''
        <div style="border: 1px solid #ddd; border-radius: 8px; overflow: hidden; max-width: 600px;">
            <!-- Hero Section Preview -->
            <div style="background: linear-gradient(135deg, {hero_start} 0%, {hero_end} 100%); 
                        padding: 20px; color: white; text-align: center;">
                <h3 style="margin: 0; color: white;">Hero Section Preview</h3>
                <p style="margin: 5px 0; color: rgba(255,255,255,0.9);">This shows the hero gradient</p>
            </div>
            
            <!-- Content Section with Primary Colors -->
            <div style="padding: 20px; background: #f8f9fa;">
                <button style="background-color: {primary}; color: white; border: none; padding: 8px 16px; 
                              border-radius: 4px; margin-right: 10px;">Primary Button</button>
                <button style="background-color: {primary_hover}; color: white; border: none; padding: 8px 16px; 
                              border-radius: 4px;">Primary Hover</button>
            </div>
            
            <!-- Footer Section -->
            <div style="background-color: {footer_bg}; color: {footer_text}; 
                        padding: 15px; text-align: center;">
                <p style="margin: 0; color: {footer_text};">Footer Preview - Contact info and links</p>
            </div>
        </div>
        '''.format(
            hero_start=obj.hero_start_color,
            hero_end=obj.hero_end_color,
            primary=obj.primary_color,
            primary_hover=obj.primary_hover_color,
            footer_bg=obj.footer_bg_color,
            footer_text=obj.footer_text_color,
        )
        return mark_safe(preview_html)
    color_preview.short_description = "Theme Preview"
    
    def activate_themes(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f"Activated {updated} theme(s).")
    activate_themes.short_description = "Activate selected themes"
    
    def deactivate_themes(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f"Deactivated {updated} theme(s).")
    deactivate_themes.short_description = "Deactivate selected themes"