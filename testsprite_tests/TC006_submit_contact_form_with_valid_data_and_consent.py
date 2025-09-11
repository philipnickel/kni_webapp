import requests

def test_submit_contact_form_with_valid_data_and_consent():
    base_url = "http://localhost:8000"
    endpoint = f"{base_url}/fa-tilbud/"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html"
    }
    form_data = {
        "name": "Test User",
        "email": "testuser@example.com",
        "phone": "12345678",
        "message": "This is a test message.",
        "consent": "true"
    }
    try:
        response = requests.post(endpoint, data=form_data, headers=headers, timeout=30, allow_redirects=False)
    except requests.RequestException as e:
        assert False, f"Request failed: {e}"

    # Expecting a redirect to thank you page with status code 302
    assert response.status_code == 302, f"Expected status code 302, got {response.status_code}"
    location = response.headers.get("Location")
    assert location is not None, "Redirect location header missing"
    assert location.endswith("/fa-tilbud/tak/") or location == "/fa-tilbud/tak/", f"Unexpected redirect location: {location}"

test_submit_contact_form_with_valid_data_and_consent()