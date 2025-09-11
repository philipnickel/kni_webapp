import requests
from requests.exceptions import RequestException

BASE_URL = "http://localhost:8000"
CREATE_PROJECT_PATH = "/admin/projects/create/"
PROJECTS_LIST_PATH = "/admin/projects/"


def test_create_new_project_with_valid_data():
    session = requests.Session()
    try:
        # Step 1: Get the create project page to obtain CSRF token
        create_page_response = session.get(BASE_URL + CREATE_PROJECT_PATH, timeout=30)
        assert create_page_response.status_code == 200, f"Expected 200 OK on GET create page, got {create_page_response.status_code}"

        # Extract CSRF token from cookies or hidden input in response content
        # Usually Django sets CSRF token in cookie named 'csrftoken'
        csrftoken = session.cookies.get('csrftoken')
        if not csrftoken:
            # Try to parse from response content (hidden input named csrfmiddlewaretoken)
            import re
            match = re.search(r'name="csrfmiddlewaretoken" value="(.+?)"', create_page_response.text)
            assert match, "CSRF token not found in form"
            csrftoken = match.group(1)

        # Prepare valid project data
        project_data = {
            "title": "New Project Title",
            "description": "This is a description for a new test project.",
            "featured": "true",  # HTML form data uses string, backend will parse boolean
            "published": "true",
            "date": "2025-09-10",
            "csrfmiddlewaretoken": csrftoken
        }

        headers = {
            "Referer": BASE_URL + CREATE_PROJECT_PATH,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        # Step 2: POST to create project with form data and CSRF token
        post_response = session.post(
            BASE_URL + CREATE_PROJECT_PATH,
            data=project_data,
            headers=headers,
            timeout=30,
            allow_redirects=False  # We want to check 302 redirect explicitly
        )

        # Validate response is a redirect (302)
        assert post_response.status_code == 302, f"Expected 302 redirect, got {post_response.status_code}"

        # Validate redirect location is to project list page
        location = post_response.headers.get("Location", "")
        assert location.endswith(PROJECTS_LIST_PATH), f"Redirect location should end with {PROJECTS_LIST_PATH}, got {location}"

    except RequestException as e:
        assert False, f"Request failed: {str(e)}"


test_create_new_project_with_valid_data()