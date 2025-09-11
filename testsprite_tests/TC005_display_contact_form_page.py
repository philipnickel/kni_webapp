import requests

BASE_URL = "http://localhost:8000"
TIMEOUT = 30

def test_display_contact_form_page():
    url = f"{BASE_URL}/fa-tilbud/"
    headers = {
        "Accept": "text/html"
    }
    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
        content_type = response.headers.get("Content-Type", "")
        assert "text/html" in content_type, f"Expected 'text/html' in Content-Type but got '{content_type}'"
        assert "<form" in response.text.lower(), "Expected to find a form in the contact page HTML"
    except requests.RequestException as e:
        assert False, f"Request failed: {e}"

test_display_contact_form_page()