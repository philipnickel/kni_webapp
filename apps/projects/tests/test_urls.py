from django.urls import reverse, resolve


def test_gallery_index_url_resolves():
    url = reverse("projects:gallery_index")
    match = resolve(url)
    assert match.url_name == "gallery_index"


def test_project_detail_url_pattern():
    match = resolve("/projekter/some-slug/")
    assert match.url_name == "project_detail"

