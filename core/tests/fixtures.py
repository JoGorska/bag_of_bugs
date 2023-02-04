# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import pytest


@pytest.fixture
def user_one():
    return User.objects.get_or_create(
        email='user.one@test.me',
        password='supersecret',
        username='user',
        first_name='User',
        last_name='One'
    )[0]
