def test_installed_apps_contains_core_apps(settings):
    apps = settings.INSTALLED_APPS
    assert "wagtail" in apps
    for app in ("apps.core", "apps.pages", "apps.projects", "apps.contacts", "apps.analytics"):
        assert app in apps

