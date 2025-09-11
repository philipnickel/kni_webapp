import requests

BASE_URL = "http://localhost:8000"
TIMEOUT = 30

def test_display_contact_form_thank_you_page():
    url = f"{BASE_URL}/fa-tilbud/tak/"
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        assert "thank you" in response.text.lower() or "tak" in response.text.lower(), "Thank you message not found in response content"
    except requests.RequestException as e:
        assert False, f"Request to {url} failed: {e}"

test_display_contact_form_thank_you_page()