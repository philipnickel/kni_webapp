import requests

BASE_URL = "http://localhost:8000"
TIMEOUT = 30
HEADERS = {
    "Accept": "text/html"
}

def test_TC009_search_pages_and_content_with_filters():
    session = requests.Session()
    url = f"{BASE_URL}/search/"
    params_sets = [
        {"query": "project"},                          # only required param
        {"query": "project", "type": "projects"},     # with type filter
        {"query": "project", "featured": "true"},     # with featured filter
        {"query": "project", "page": 1},              # with page param
        {"query": "project", "type": "projects", "featured": "true", "page": 1}  # all filters
    ]
    for params in params_sets:
        try:
            response = session.get(url, headers=HEADERS, params=params, timeout=TIMEOUT)
        except requests.RequestException as e:
            assert False, f"Request failed with exception: {e}"
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code} for params {params}"
        content_type = response.headers.get("Content-Type", "")
        assert "text/html" in content_type, f"Expected 'text/html' content type but got '{content_type}' for params {params}"

        html_text = response.text

        # Check that the response is not empty and contains the query term somewhere
        assert html_text and params["query"].lower() in html_text.lower(), f"Response HTML does not contain query term '{params['query']}' for params {params}"

        if "page" in params or "pagination" in html_text:
            assert ("pagination" in html_text or "aria-label=\"Pagination\"" in html_text), f"Pagination element expected but not found for params {params}"

        if "type" in params or "featured" in params:
            assert ("filters" in html_text or "filter" in html_text), f"Filter UI or indicators expected but not found for params {params}"

test_TC009_search_pages_and_content_with_filters()
