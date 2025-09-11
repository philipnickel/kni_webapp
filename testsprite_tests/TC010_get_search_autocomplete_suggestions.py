import requests

def test_get_search_autocomplete_suggestions():
    base_url = "http://localhost:8000"
    endpoint = "/search/autocomplete/"
    params = {'q': 'te'}
    headers = {
        'Accept': 'application/json'
    }
    try:
        response = requests.get(f"{base_url}{endpoint}", params=params, headers=headers, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        assert False, f"Request to {endpoint} failed: {e}"

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    try:
        data = response.json()
    except ValueError:
        assert False, "Response is not valid JSON"

    assert isinstance(data, dict), "Response JSON root should be an object"
    assert 'suggestions' in data, "Response JSON missing 'suggestions' key"
    suggestions = data['suggestions']
    assert isinstance(suggestions, list), "'suggestions' should be a list"

    for suggestion in suggestions:
        assert isinstance(suggestion, dict), "Each suggestion should be a dict"
        assert 'title' in suggestion and isinstance(suggestion['title'], str), "Suggestion missing 'title' or not string"
        assert 'url' in suggestion and isinstance(suggestion['url'], str), "Suggestion missing 'url' or not string"
        assert 'type' in suggestion and isinstance(suggestion['type'], str), "Suggestion missing 'type' or not string"

test_get_search_autocomplete_suggestions()