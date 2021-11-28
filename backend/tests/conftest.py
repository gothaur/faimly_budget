import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from budget.models import Budget, Category

User = get_user_model()

from rest_framework.authtoken.models import Token


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    user = User.objects.filter(username='username').first()
    if user is None:
        user = User.objects.create_user(username='username', password='secret')
    return user


@pytest.fixture
def token(db, user):
    token, _ = Token.objects.get_or_create(user=user)
    return token


@pytest.fixture
def client_with_logged_in_user(db, api_client, user, token):
    api_client.login(username='username', password='secret')
    yield api_client


@pytest.fixture
def budget(user):
    budget, _ = Budget.objects.get_or_create(name='budget 1', owner=user)
    return budget


@pytest.fixture
def category():
    category, _ = Category.objects.get_or_create(name='category 1')
    return category