from datetime import date

import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    'url, kwargs', [
        ('api:expenses-list', {'budget_pk': '1'}), ('api:expenses-create', {'budget_pk': '1'}),
        ('api:expenses-details', {'budget_pk': '1', 'pk': '1'})]
)
@pytest.mark.django_db
def test_unauthorized_request(api_client, budget, url, kwargs):
    url = reverse(url, kwargs=kwargs)
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_can_list_expenses(client_with_logged_in_user, budget):
    response = client_with_logged_in_user.get(
        reverse('api:expenses-list', kwargs={'budget_pk': budget.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_can_create_expense(client_with_logged_in_user, budget, category):
    expense = {
        'date': date.today(),
        'amount': 12.34,
        'description': 'this is some description',
        'category': category,
    }
    response = client_with_logged_in_user.post(
        reverse('api:expenses-create', kwargs={'budget_pk': budget.pk}), expense)
    assert response.status_code == 201

    assert response.data['description'] == 'this is some description'
    assert response.data['amount'] == '12.34'
    assert response.data['budget'] == 'budget 1'
