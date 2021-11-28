from datetime import date

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


@pytest.mark.parametrize(
    'url, kwargs', [
        ('api:expenses-list', {}), ('api:expenses-create', {}),
        ('api:expenses-details', {'pk': '1'})]
)
def test_unauthorized_request(api_client, url, kwargs):
    url = reverse(url, kwargs=kwargs)
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_can_list_expenses(client_with_logged_in_user):
    response = client_with_logged_in_user.get(reverse('api:expenses-list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_can_create_expense(client_with_logged_in_user, budget, category):
    expense = {
        'date': date.today(),
        'amount': 12.34,
        'description': 'this is some description',
        'budget': budget.pk,
        'category': category,
    }
    response = client_with_logged_in_user.post(reverse('api:expenses-create'), expense)
    assert response.status_code == 201

    assert response.data['description'] == 'this is some description'
    assert response.data['amount'] == '12.34'
    assert response.data['budget'] == 1
