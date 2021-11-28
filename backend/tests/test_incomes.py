from datetime import date

import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    'url, kwargs', [
        ('api:incomes-list', {'budget_pk': '1'}), ('api:income-create', {'budget_pk': '1'}),
        ('api:income-details', {'budget_pk': '1', 'pk': '1'})]
)
@pytest.mark.django_db
def test_unauthorized_request(api_client, budget, url, kwargs):
    url = reverse(url, kwargs=kwargs)
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_can_list_incomes(client_with_logged_in_user, budget):
    response = client_with_logged_in_user.get(reverse('api:incomes-list', kwargs={'budget_pk': budget.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_can_create_income(client_with_logged_in_user, budget):
    income = {
        'date': date.today(),
        'amount': 12345.67,
        'description': 'this is some description',
        'budget': budget.pk,
    }
    response = client_with_logged_in_user.post(reverse('api:income-create', kwargs={'budget_pk': budget.pk}), income)
    assert response.status_code == 201

    assert response.data['description'] == 'this is some description'
    assert response.data['amount'] == '12345.67'
    assert response.data['owner'] == 'username'
    assert response.data['budget'] == 'budget 1'
