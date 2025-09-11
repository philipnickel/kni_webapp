import requests

def test_list_all_projects_admin_view():
    base_url = "http://localhost:8000"
    endpoint = "/admin/projects/"
    url = base_url + endpoint
    timeout = 30

    # Admin credentials - replace with valid admin username and password
    admin_auth = ('admin', 'adminpassword')

    headers = {
        "Accept": "text/html",
    }

    try:
        response = requests.get(url, headers=headers, auth=admin_auth, timeout=timeout)
    except requests.RequestException as e:
        assert False, f"Request to {url} failed: {e}"

    # Validate response status code is 200 for authorized admin access
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Validate content type is HTML
    content_type = response.headers.get("Content-Type", "")
    assert "text/html" in content_type, f"Expected 'text/html' in Content-Type, got {content_type}"

    # Validate pagination by checking presence of typical pagination elements in HTML
    html = response.text.lower()
    assert ("pagination" in html or "page" in html), "Response HTML does not appear to contain pagination elements"

# Run the test function
test_list_all_projects_admin_view()