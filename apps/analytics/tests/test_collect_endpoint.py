import json
import pytest


@pytest.mark.skip(reason="Requires DB + Wagtail Site; enable after migrations")
def test_collect_endpoint_smoke(client):
    resp = client.post("/analytics/collect", data=json.dumps({"type": "pageview", "path": "/"}), content_type="application/json")
    assert resp.status_code in (200, 400)

