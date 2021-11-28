import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_can_create_user(api_client):
    url = reverse("api:register-user")
    user_data = {
        'username': 'username',
        'password': 'Qwertyuiop!234567890'
    }
    response = api_client.post(url, user_data)
    assert response.status_code == 201

    assert response.data['username'] == user_data['username']
