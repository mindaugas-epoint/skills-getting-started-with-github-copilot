from src.app import activities


def test_get_activities_returns_all_activities_and_no_store_header(client):
    response = client.get("/activities")

    assert response.status_code == 200
    assert response.headers["cache-control"] == "no-store"
    assert response.json() == activities
