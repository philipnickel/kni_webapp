# JCleemann Byg

Modern Danish construction business website built with Django & Wagtail CMS.

## Quick Start

```bash
make setup    # Install & setup database
make run      # Start server
```

**Access:**
- Website: http://localhost:8000  
- Admin: http://localhost:8000/admin  
- Login: `testadmin` / `test123`

## Features

- **Project Gallery** - Construction work showcase
- **Admin Interface** - Easy content management  
- **Contact Forms** - Quote requests
- **Responsive** - Mobile-friendly design
- **Danish Language** - Localized interface

## Commands

```bash
make help     # Show all commands
make setup    # One-time setup  
make run      # Start development server
make admin    # Create new admin user
make clean    # Remove generated files
```

## Structure

```
├── apps/           # Django applications
│   ├── core/       # Wagtail customization
│   ├── pages/      # Homepage & content
│   ├── projects/   # Project management
│   └── contacts/   # Contact forms
├── static/         # CSS, JS, images
├── templates/      # HTML templates
├── media/          # User uploads
└── project/        # Django settings
```

## Admin Features

- Custom wood construction theme
- Project management with image galleries  
- Mobile responsive interface
- User-friendly content editing

---

**Stack:** Django 5.0 • Wagtail CMS • Tailwind CSS  
**Language:** Danish