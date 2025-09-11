import requests

def test_get_home_page_content():
    base_url = "http://localhost:8000"
    url = f"{base_url}/"
    headers = {
        "Accept": "text/html"
    }
    try:
        response = requests.get(url, headers=headers, timeout=30)
        # Assert status code 200
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        # Assert content type is HTML
        content_type = response.headers.get("Content-Type", "")
        assert "text/html" in content_type, f"Expected Content-Type to contain 'text/html', got '{content_type}'"
        content = response.text.lower()
        # Check presence of key modular content blocks in HTML content, heuristically by substrings
        # Hero sections
        assert any(keyword in content for keyword in ["hero-section", "hero", "welcome"]), "Hero section not found in homepage content"
        # Featured projects
        assert any(keyword in content for keyword in ["featured project", "featured-project", "featured projects", "featured_projects", "featuredproject"]), "Featured projects section not found"
        # Testimonials
        assert any(keyword in content for keyword in ["testimonial"]), "Testimonials section not found"
        # Call-to-action sections
        assert any(keyword in content for keyword in ["call to action", "cta", "call-to-action"]), "Call-to-action section not found"
    except requests.RequestException as e:
        assert False, f"Request failed: {e}"

test_get_home_page_content()
