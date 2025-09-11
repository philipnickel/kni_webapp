# KNI Webapp - Product Requirements Document

## 1. Project Overview

**Project Name**: KNI Webapp  
**Type**: Construction Business Website with Content Management System  
**Framework**: Django 4.2 + Wagtail CMS 7.1  
**Language**: Danish (da)  
**Database**: PostgreSQL  

### 1.1 Purpose
A professional construction business website built with Django and Wagtail CMS, designed for "JCleemann Byg" - a Danish construction company. The platform provides project portfolio management, client contact functionality, and content management capabilities.

### 1.2 Target Users
- **Primary**: Potential clients looking for construction services
- **Secondary**: Business owner/admin managing content and projects
- **Tertiary**: Search engines and web crawlers

## 2. Technical Architecture

### 2.1 Technology Stack
- **Backend**: Python 3.13, Django 4.2
- **CMS**: Wagtail 7.1
- **Database**: PostgreSQL 15
- **Frontend**: HTML5, CSS3, JavaScript, HTMX
- **Media Processing**: Pillow (Python Imaging Library)
- **Static Files**: WhiteNoise
- **Search**: Wagtail's database search backend
- **Deployment**: Docker-ready with docker-compose.yml

### 2.2 Key Dependencies
```
django>=4.2,<5.1
wagtail>=7.1,<7.2
psycopg2-binary>=2.9
Pillow>=10.0
django-htmx>=1.17
python-dotenv>=1.0
whitenoise>=6.6
```

## 3. Core Features & Functionality

### 3.1 Project Management System

#### 3.1.1 Legacy Project Model
- **Purpose**: Original project management system
- **Fields**: Title, slug, description, materials, client info, location, featured status, publication status, date, tags
- **Capabilities**: Image gallery, search indexing, admin interface

#### 3.1.2 New ProjectPage Model (Wagtail-native)
- **Enhanced Features**: 
  - Workflow management (draft, review, publish)
  - Collection-based categorization
  - Priority levels (low, medium, high, urgent)
  - Project status tracking (planning, in_progress, completed, on_hold, cancelled)
  - Budget estimation and tracking
  - Revision history
  - Advanced permissions system

#### 3.1.3 Project Images
- **Multiple images per project**
- **Image optimization and resizing**
- **Caption and alt-text support**
- **Sortable image ordering**

### 3.2 Content Management (Wagtail CMS)

#### 3.2.1 Page Types
- **HomePage**: Modular content with StreamField blocks
- **GalleryPage**: Project portfolio display with filtering
- **ContactPage**: Contact information and form integration
- **ModularPage**: Flexible content pages with reusable blocks

#### 3.2.2 StreamField Blocks
- Hero sections (v2 with enhanced features)
- Trust badges
- Featured projects showcase
- Services grid (inline and standard)
- Call-to-action sections
- Features blocks
- Rich text sections
- Testimonials (snippet-based)
- Logo cloud
- FAQ sections
- Image galleries

#### 3.2.3 Reusable Snippets
- **Testimonials**: Customer quotes with name and role
- **Logos**: Partner/client logos with optional URLs
- **Services**: Service descriptions for reuse across pages

### 3.3 Contact System

#### 3.3.1 Contact Form
- **Fields**: Name, email, phone, message, consent checkbox
- **Validation**: Django form validation with CSRF protection
- **Storage**: ContactSubmission model with status tracking
- **Workflow**: Form → Validation → Storage → Thank you page

#### 3.3.2 Contact Management
- **Status tracking**: New, In Progress, Closed
- **Site association**: Multi-site support ready
- **Admin interface**: Built-in Django admin integration

### 3.4 Search Functionality

#### 3.4.1 Full-Text Search
- **Scope**: All published pages and content
- **Features**: Query logging, search promotions
- **Filtering**: By page type, featured status
- **Pagination**: 10 results per page

#### 3.4.2 Autocomplete Search
- **Real-time suggestions** (minimum 2 characters)
- **Multi-source**: Pages and projects
- **JSON API response**
- **Type indicators** for different content types

### 3.5 Site Configuration

#### 3.5.1 Site Settings (Wagtail Settings)
- **Company Information**: Name, logo, contact details, CVR number
- **Theme Settings**: Color scheme selection (Forest, Wood, Slate)
- **Typography**: Font combination choices
- **Navigation**: CTA button configuration
- **Footer**: Rich content areas, social media links, opening hours
- **Preview Settings**: Preview URL configuration

#### 3.5.2 Multi-language Support
- **Primary Language**: Danish (da)
- **Timezone**: Europe/Copenhagen
- **Internationalization**: Django i18n framework ready

## 4. User Interface & Experience

### 4.1 Design System
- **Themes**: Forest (default), Wood, Slate
- **Typography Options**:
  - Inter + Playfair Display (Professional)
  - Inter + Georgia (Classic)
  - System fonts (Fast loading)
  - Roboto + Lora (Modern)
  - Open Sans + Merriweather (Readable)

### 4.2 Responsive Design
- **Mobile-first approach**
- **Progressive enhancement**
- **Touch-friendly interfaces**
- **Optimized image delivery**

### 4.3 Performance Features
- **Static file optimization** with WhiteNoise
- **Image optimization** with Pillow
- **Lazy loading** for images
- **Efficient database queries**
- **Search indexing** for fast content discovery

## 5. Administrative Features

### 5.1 Wagtail Admin Interface
- **Rich text editing** with Draftail
- **Page tree management**
- **Workflow system** (draft → review → publish)
- **User permissions** and groups
- **Site-wide settings** management

### 5.2 Project-Specific Admin
- **Custom project dashboard**
- **Bulk actions** for project management
- **Advanced filtering** and search
- **Project status indicators**
- **Budget tracking interface**

### 5.3 Content Workflow
- **Draft → Review → Publish** cycle
- **Revision history** and rollback
- **Scheduled publishing**
- **Content locking** during editing

## 6. Security & Compliance

### 6.1 Security Measures
- **CSRF protection** on all forms
- **SQL injection prevention** via Django ORM
- **XSS protection** with template auto-escaping
- **Secure headers** configuration
- **HTTPS enforcement** (production)

### 6.2 Data Protection
- **GDPR-compliant** contact forms
- **Consent tracking** for form submissions
- **Data retention** policies ready
- **User data export** capabilities

## 7. SEO & Marketing

### 7.1 Search Engine Optimization
- **Meta tags** management per page
- **Structured data** markup
- **XML sitemap** generation
- **Social media** integration
- **Search-friendly URLs**

### 7.2 Analytics & Tracking
- **Search query logging**
- **Popular content** identification
- **User journey** tracking ready
- **Conversion funnel** optimization

## 8. Integration Points

### 8.1 External Services
- **Email delivery** (ready for SMTP/API integration)
- **Social media** links and sharing
- **Analytics platforms** (Google Analytics ready)
- **CDN integration** (optional)

### 8.2 API Readiness
- **REST API** potential via Django REST Framework
- **Wagtail API** for headless CMS usage
- **Webhook support** for external integrations

## 9. Deployment & Infrastructure

### 9.1 Development Environment
- **Docker Compose** configuration
- **PostgreSQL 15** container
- **Environment variables** configuration
- **Debug mode** settings

### 9.2 Production Readiness
- **Static file** serving optimization
- **Database** connection pooling
- **Caching** framework integration ready
- **Monitoring** and logging hooks

### 9.3 Scalability Considerations
- **Database indexing** for performance
- **Media file** optimization
- **Search backend** scalability
- **Multi-site** architecture support

## 10. Testing Requirements

### 10.1 Functional Testing
- **Form submission** workflows
- **Content management** operations
- **Search functionality**
- **Image upload** and processing
- **User authentication** and permissions

### 10.2 Performance Testing
- **Page load times**
- **Database query** optimization
- **Image delivery** performance
- **Search response** times

### 10.3 Security Testing
- **Form validation** bypass attempts
- **SQL injection** prevention
- **XSS attack** prevention
- **CSRF token** validation
- **File upload** security

## 11. Success Metrics

### 11.1 Technical Metrics
- **Page load time** < 3 seconds
- **Search response** < 500ms
- **Image optimization** > 80% compression
- **SEO score** > 90/100

### 11.2 Business Metrics
- **Contact form** conversion rate
- **Project portfolio** engagement
- **Search usage** and success rate
- **Content management** efficiency

## 12. Future Enhancements

### 12.1 Planned Features
- **Multi-language** content support
- **Advanced workflow** automation
- **Client portal** integration
- **Mobile app** API support
- **Advanced analytics** dashboard

### 12.2 Integration Opportunities
- **CRM system** integration
- **Project management** tools
- **Accounting software** connection
- **Marketing automation** platforms
- **Customer feedback** systems

---

**Document Version**: 1.0  
**Last Updated**: January 2025  
**Status**: Active Development  
**Review Cycle**: Monthly
