import requests
from requests.exceptions import RequestException

BASE_URL = "http://localhost:8000"
TIMEOUT = 30

def test_get_project_details_by_slug():
    session = requests.Session()
    headers = {
        "Accept": "text/html",
    }

    created_slug = None

    try:
        # Step 1: Create a new project to have an existing project slug
        create_url = f"{BASE_URL}/admin/projects/create/"
        # Use form-urlencoded payload with valid minimal project data
        # Using a unique title to avoid conflicts
        create_data = {
            "title": "Test Project For TC004",
            "description": "Temporary project created for testing get project details by slug.",
            "featured": "false",
            "published": "true",
            "date": "2024-01-01"
        }
        # Create project (expect redirect status 302)
        create_response = session.post(create_url, data=create_data, timeout=TIMEOUT)
        assert create_response.status_code == 302, f"Expected 302 on project create, got {create_response.status_code}"

        # Step 2: Retrieve the project list to find the slug of the created project
        list_url = f"{BASE_URL}/admin/projects/"
        list_response = session.get(list_url, headers=headers, timeout=TIMEOUT)
        assert list_response.status_code == 200, f"Expected 200 on project list, got {list_response.status_code}"
        # Parse the slug from the list page HTML (simple extraction)
        # We assume the slug appears in URLs like /projekter/{slug}/ somewhere in the HTML
        # We'll search for the project title and extract adjacent slug URL
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(list_response.text, "html.parser")

        project_slug = None
        # Find all links matching /projekter/{slug}/ pattern
        anchors = soup.find_all("a", href=True)
        for a in anchors:
            href = a['href']
            if href.startswith("/projekter/") and href.endswith("/"):
                # Check if the anchor text or nearby text matches the project title
                # or just take the first project link found
                if "Test Project For TC004" in a.text:
                    # Extract slug
                    slug_candidate = href.split("/")[2]
                    project_slug = slug_candidate
                    break

        # If not found by anchor text match, fallback to first project link
        if not project_slug:
            for a in anchors:
                href = a['href']
                if href.startswith("/projekter/") and href.endswith("/"):
                    project_slug = href.split("/")[2]
                    break

        assert project_slug is not None, "Failed to find the created project's slug in the project list"
        created_slug = project_slug

        # Step 3: Make GET request to /projekter/{slug}/ for existing project
        project_detail_url = f"{BASE_URL}/projekter/{created_slug}/"
        detail_response = session.get(project_detail_url, headers=headers, timeout=TIMEOUT)
        assert detail_response.status_code == 200, f"Expected 200 status for existing project details, got {detail_response.status_code}"
        assert 'text/html' in detail_response.headers.get('Content-Type', ''), "Response is not HTML content for existing project"

        # Step 4: Test non-existing slug returns 404
        nonexistent_slug = "nonexistent-slug-for-tc004-test"
        nonexistent_url = f"{BASE_URL}/projekter/{nonexistent_slug}/"
        not_found_response = session.get(nonexistent_url, headers=headers, timeout=TIMEOUT)
        assert not_found_response.status_code == 404, f"Expected 404 for non-existent project slug, got {not_found_response.status_code}"

    except RequestException as e:
        assert False, f"Request failed: {e}"
    finally:
        # Cleanup: Attempt to delete the created project via admin interface if possible
        # Since no delete endpoint is specified in PRD, skip actual deletion
        # Placeholder for cleanup logic if API expands
        pass

test_get_project_details_by_slug()