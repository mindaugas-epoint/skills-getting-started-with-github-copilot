from src.app import activities


def test_unregister_removes_participant_and_returns_success_message(client):
    activity_name = "Chess Club"
    email = "daniel@mergington.edu"

    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.headers["cache-control"] == "no-store"
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}
    assert email not in activities[activity_name]["participants"]


def test_unregister_returns_404_for_unknown_activity(client):
    response = client.delete(
        "/activities/Unknown%20Club/participants",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_returns_404_when_student_is_not_signed_up(client):
    response = client.delete(
        "/activities/Chess%20Club/participants",
        params={"email": "not.signed.up@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Student is not signed up for this activity"}
