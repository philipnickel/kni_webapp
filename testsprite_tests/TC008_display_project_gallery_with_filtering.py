import requests

BASE_URL = "http://localhost:8000"
TIMEOUT = 30
HEADERS = {
    "Accept": "text/html"
}

def test_display_project_gallery_with_filtering():
    try:
        # Test without query parameters
        url = f"{BASE_URL}/gallery/"
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        content = response.text
        # Basic check for presence of project collections content
        assert "project" in content.lower() or "gallery" in content.lower(), "Gallery page content does not appear to be correct"
        
        # Test with featured filter
        params = {"featured": "true"}
        response = requests.get(url, headers=HEADERS, params=params, timeout=TIMEOUT)
        assert response.status_code == 200, f"Featured filter: Expected status code 200, got {response.status_code}"
        content = response.text
        assert "project" in content.lower() or "gallery" in content.lower(), "Featured filtered gallery content missing expected elements"
        
        # Test with tag filter (example tag)
        params = {"tag": "construction"}
        response = requests.get(url, headers=HEADERS, params=params, timeout=TIMEOUT)
        assert response.status_code == 200, f"Tag filter: Expected status code 200, got {response.status_code}"
        content = response.text
        assert "project" in content.lower() or "gallery" in content.lower(), "Tag filtered gallery content missing expected elements"
        
        # Test with both featured and tag filters
        params = {"featured": "true", "tag": "construction"}
        response = requests.get(url, headers=HEADERS, params=params, timeout=TIMEOUT)
        assert response.status_code == 200, f"Featured + Tag filter: Expected status code 200, got {response.status_code}"
        content = response.text
        assert "project" in content.lower() or "gallery" in content.lower(), "Combined filtered gallery content missing expected elements"
    except requests.RequestException as e:
        assert False, f"RequestException occurred: {str(e)}"

test_display_project_gallery_with_filtering()